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
            'number_of_bookings',
            ]
