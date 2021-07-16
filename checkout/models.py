import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=6, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    house_number = models.CharField(max_length=10, null=False, blank=False)
    postcode = models.CharField(max_length=6, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    # generate unique order number
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    # update grand total
    def update_total(self):
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    # make sure saved order has order number
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

# set lineitem total and update order total
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

