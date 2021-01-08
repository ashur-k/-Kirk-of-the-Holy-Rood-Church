from django import forms
from .models import CurrentColorTheme


class CurrentColorThemeForm(forms.ModelForm):

    class Meta:
        model = CurrentColorTheme
        fields = ['current_color_theme']