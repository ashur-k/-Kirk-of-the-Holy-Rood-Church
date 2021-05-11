from django import forms
from .models import Notice, NewsLetter


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = [
            'notice_title',
            'notice_given_by',
            'notice_context',
            'contact_phone_number',
            'contact_email',
            'date_time',
            'notice_display_status',
        ]


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = [
            'title',
            'upload',
            'description',
        ]
