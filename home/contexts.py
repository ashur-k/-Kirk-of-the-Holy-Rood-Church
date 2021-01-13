from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import CurrentColorTheme
from .forms import CurrentColorThemeForm
from django.contrib import messages


def site_settings(request):
    color = get_object_or_404(CurrentColorTheme, id=1)
    if request.method == 'POST':
        color_theme_form = CurrentColorThemeForm(request.POST, instance=color)
        if color_theme_form.is_valid():
            color_theme_form.save()
            messages.success(request, 'Successfully updated theme.')

    color_theme_form = CurrentColorThemeForm(instance=color)

    context = {
        'color': color,
        'color_theme_form': color_theme_form,
    }

    return context
