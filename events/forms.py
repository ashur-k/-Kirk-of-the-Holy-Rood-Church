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


class EventForm(forms.Form):
    STATUS = (
        ('True', 'Show'),
        ('False', 'Dont Show'),
    )
    event_name = forms.CharField(max_length=254)
    image = forms.forms.FileField()
    event_description = forms.CharField(widget=forms.Textarea)
    event_dates = forms.CharField(max_length=254)
    event_price = forms.CharField(max_length=25)
    event_display_status = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=STATUS)
    event_instructions = forms.CharField(max_length=254)
