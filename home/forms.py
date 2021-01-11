from django import forms
from .models import CurrentColorTheme, HeroSectionText


class CurrentColorThemeForm(forms.ModelForm):

    class Meta:
        model = CurrentColorTheme
        fields = ['current_color_theme']


class HeroSectionTextForm(forms.ModelForm):

    class Meta:
        model = HeroSectionText
        hero_heading = forms.CharField(widget=forms.Textarea)
        fields = ['hero_heading']

        widgets = {
            'hero_heading': forms.Textarea(attrs={'rows': 5, 'cols': 10})
        }
