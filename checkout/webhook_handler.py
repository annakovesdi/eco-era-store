from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWebhookHandler():
    def __init__(self, request):
        self.request = request

    # send confirmation email
    def _send_confirmation_email(self, order):
        client_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt'
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [client_email]
        )

    # handle generic webhook event
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook recieved {event["type"]}',
            status=200,
        )

    # handle payment_intent.succeeded event
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        payment_id = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # if save_info is checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            if save_info:
                profile = UserProfile.objects.get(user__username=username)
                profile.default_full_name = shipping_details.name
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address = shipping_details.address.line1
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_city = shipping_details.address.city
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt < 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    phone_number__iexact=shipping_details.phone,
                    street_address__iexact=shipping_details.address.line1,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_payment_id=payment_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} SUCCESS: '
                'Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=shipping_details.name,
                    phone_number=shipping_details.phone,
                    street_address=shipping_details.address.line1,
                    house_number=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    country=shipping_details.address.country,
                    original_bag=bag,
                    stripe_payment_id=payment_id,
                )
                for item_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook recieved {event["type"]} Error! {e}',
                        status=500,
                    )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook recieved {event["type"]} Success! '
                    'Created order in webhook',
            status=200,
        )

    # handle payment_intent.payment_failed event
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook recieved {event["type"]}',
            status=200,
        )
