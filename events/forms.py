from django import forms
from .models import (
    Events,
    EventDates,
    )


class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = [
            'event_name',
            'image',
            'event_description',
            'event_price',
            'event_ticket_quantity',
            'event_display_status',
            'event_display_status'
            ]


class EventDateForm(forms.ModelForm):
    class Meta:
        model = EventDates
        fields = ['date']
