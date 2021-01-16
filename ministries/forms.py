from django import forms
from .models import (
    Message,
    Ministries,
    )


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            'full_name',
            'email',
            'phone_number',
            'message',
            'street_address1',
            'street_address2',
            'postcode',
            ]
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'cols': 0}
            ))


class MinistrieForm(forms.ModelForm):

    class Meta:
        model = Ministries
        fields = '__all__'

