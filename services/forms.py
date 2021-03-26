from django import forms
from .models import (
    SundayServiceInformation
    )


class SundayServiceInformationForm(forms.ModelForm):

    class Meta:
        model = SundayServiceInformation
        fields = [
            'title',
            'preacher_name',
            'sermon_title',
            'bible_refrence',
            'worship_hymm1',
            'worship_hymm2',
            'worship_hymm3',
            'worship_hymm4',
            'important_notices',
            'date'
            ]
