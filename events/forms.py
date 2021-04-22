from django import forms
from .models import (
    Events,
    EventDates,
    BookingFreeEvents
    )


class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = [
            'event_name',
            'image',
            'event_description',
            'event_price',
            'is_free_event',
            'event_display_status',
            'event_display_status'
            ]


class EventDateForm(forms.ModelForm):
    class Meta:
        model = EventDates
        fields = [
            'total_tickets',
            'date'
            ]


class BookingFreeEventsForm(forms.ModelForm):

    class Meta:
        model = BookingFreeEvents
        fields = [
            'full_name',
            'email',
            'phone_number',
            ]

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
