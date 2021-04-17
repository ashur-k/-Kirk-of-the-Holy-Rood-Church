from django import forms
from .models import (
    SundayServiceInformation,
    SundayServiceBooking
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
            'available_bookings',
            'important_notices',
            'date'
            ]


class SundayServiceBookingForm(forms.ModelForm):

    class Meta:
        model = SundayServiceBooking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'number_of_bookings',
            ]
