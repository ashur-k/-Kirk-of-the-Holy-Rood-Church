from django import forms
from .models import (
    CurrentColorTheme,
    HeroSectionText,
    CarouselSectionText,
    CarouselInnerSection,
    SecondParallaxSection,
    StudyGroupText,
    )
from django.forms import ModelForm


class CurrentColorThemeForm(forms.ModelForm):

    class Meta:
        model = CurrentColorTheme
        fields = ['current_color_theme']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['current_color_theme'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'current_color_theme':
                self.fields[field].widget.attrs['class'] = 'form-select m-1'


class HeroSectionTextForm(forms.ModelForm):

    class Meta:
        model = HeroSectionText
        hero_heading = forms.CharField(widget=forms.Textarea)
        fields = ['hero_heading']

        widgets = {
            'hero_heading': forms.Textarea(attrs={'rows': 5, 'cols': 10})
        }


class CarouselSectionTextForm(forms.ModelForm):

    class Meta:
        model = CarouselSectionText
        heading = forms.CharField(widget=forms.Textarea)
        fields = ['heading', 'paragraph']

        widgets = {
            'paragraph': forms.Textarea(attrs={'rows': 5, 'cols': 10})
        }


class AddNewCarouselForm(ModelForm):

    class Meta:
        model = CarouselInnerSection
        heading = forms.CharField(widget=forms.Textarea)
        fields = ['heading', 'paragraph', 'carousel_image']

        widgets = {
            'paragraph': forms.Textarea(attrs={'rows': 5, 'cols': 10})
        }


class CarouselInnerSectionForm(ModelForm):

    class Meta:
        model = CarouselInnerSection
        fields = ['carousel_image', 'heading', 'paragraph']


class SecondParallaxSectionForm(ModelForm):

    class Meta:
        model = SecondParallaxSection
        fields = ['title', 'main_paragraph', 'instruction_paragraph']


class StudyGroupTextForm(forms.ModelForm):

    class Meta:
        model = StudyGroupText
        heading = forms.CharField(widget=forms.Textarea)
        fields = ['heading', 'paragraph']
