from django import forms
from .models import (
    SundayServiceInformation,
    SundayServiceBooking,
    Videos,
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

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'number_of_bookings': 'number_of_bookings',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black m-1'

            self.fields[field].label = False


class VideoForm(forms.ModelForm):

    class Meta:
        model = Videos
        fields = [
            'title',
            'video',
            'video_image',
            'main_paragraph',
            'status',
            'pinned',
            'date',
            ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'video title',
            'video': 'https://www.youtube.com/embed/PJbQN6WSkew',
            'video_image': 'video_image',
            'main_paragraph': 'video description',
            'status': 'status',
            'pinned': 'pinned',
            'date': 'date',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black m-1'

            self.fields[field].label = False
