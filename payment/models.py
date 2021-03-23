import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Sum
from django.db import models
from events.models import Events


class Payment(models.Model):
    payment_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = phone_number = PhoneNumberField()
    date = models.DateTimeField(auto_now_add=True)
    donation_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    ticket_payment_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_payment_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.ticket_payment_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.ticket_payment_total + self.donation_payment_amount
        self.save()

    def save(self, *args, **kwargs):
        '''
            By checking self.ticket payment total = 0, If there are no payments
            made for ticket then self.grandtotal gets updated too because if
            there are no tickets payment then update totla method is not called
        '''
        if self.ticket_payment_total == 0:
            self.grand_total = self.donation_payment_amount
            + self.ticket_payment_total
        if not self.payment_number:
            self.payment_number = self._generate_payment_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_number


class TicketsPayment(models.Model):
    payment = models.ForeignKey(Payment, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    event = models.ForeignKey(Events, null=False, blank=False, on_delete=models.CASCADE)
    event_date = models.CharField(max_length=150)
    event_ticket_qty = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.event.event_price * self.event_ticket_qty
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.event.event_name} on order {self.payment.payment_number}'
