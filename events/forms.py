from django import forms
from .models import (
    Events,
    )


class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = [
            'event_name',
            'image',
            'event_description',
            'event_dates',
            'event_price',
            'event_display_status',
            'event_display_status'

            ]


