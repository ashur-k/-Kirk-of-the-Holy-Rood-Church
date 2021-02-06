import uuid
from django.db.models import Sum
from django.db import models
from events.models import Events


class Payment(models.Model):
    payment_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    donation_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_payment_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        pass

    def save(self, *args, **kwargs):
        if not self.payment_number:
            self.payment_number = self._generate_payment_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_number


class TicketsPayment(models.Model):
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, null=True, blank=True, on_delete=models.CASCADE)
    event_ticket_qty = models.IntegerField(null=False, blank=False, default=1)
    payment_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.payment_total = self.event.event_price * self.event_ticket_qty
        super().save(*args, **kwargs)