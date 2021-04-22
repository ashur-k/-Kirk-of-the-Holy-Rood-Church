from django import forms
from .models import Payment, TicketsPayment
from events.models import EventDates


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = (
            'full_name',
            'email',
            'phone_number',
            'donation_payment_amount'
            )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'donation_payment_amount': 'donation_payment_amount',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black m-1'

            self.fields[field].label = False


class TicketPaymentForm(forms.ModelForm):
    class Meta:
        model = TicketsPayment
        fields = (
            'event_ticket_qty',
            'event_date',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
