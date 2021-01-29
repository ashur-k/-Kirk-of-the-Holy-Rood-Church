import uuid
from django.db.models import Sum
from django_countries.fields import CountryField
from django.db import models
from events.models import Events


class Payment(models.Model):
    payment_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *',  null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    payment_total_amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_payment_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.payment_number:
            self.order_number = self._generate_payment_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_number


class PaymentLineItem(models.Model):
    payment = models.ForeignKey(Payment, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    event = models.ForeignKey(Events, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.event.event_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.event.event_name} on order {self.payment.payment_number}'
