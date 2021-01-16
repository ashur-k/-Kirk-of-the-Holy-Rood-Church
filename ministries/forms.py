from django import forms
from .models import (
    AlphaGroup,
    )


class AlphaGroupEntranceForm(forms.ModelForm):

    class Meta:
        model = AlphaGroup
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
