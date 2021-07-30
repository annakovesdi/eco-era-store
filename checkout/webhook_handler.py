from django.http import HttpResponse


class StripeWebhookHandler():
    def __init__(self, request):
        self.request = request

    # handle generic webhook event
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook recieved {event["type"]}',
            status=200,
        )

    # handle payment_intent.succeeded event
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved {event["type"]}',
            status=200,
        )

    # handle payment_intent.payment_failed event
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook recieved {event["type"]}',
            status=200,
        )
