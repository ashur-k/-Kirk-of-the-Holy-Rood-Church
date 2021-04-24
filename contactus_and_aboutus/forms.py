from django import forms
from .models import (
    Contactus,
    )


class ContactusForm(forms.ModelForm):

    class Meta:
        model = Contactus
        fields = [
            'name',
            'email',
            'message',
            ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black m-1'

            self.fields[field].label = False
