from django import forms
from .models import (
    Contactus,
    )


class ContactusForm(forms.ModelForm):

    class Meta:
        model = Contactus
        fields = [
            'full_name',
            'email',
            'message',
            ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'message': 'Message',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black m-1'

            self.fields[field].label = False
