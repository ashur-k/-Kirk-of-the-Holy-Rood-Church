from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import CurrentColorTheme
from .forms import CurrentColorThemeForm


def site_settings(request):
    color = get_object_or_404(CurrentColorTheme, id=1)
    if request.method == 'POST':
        form = CurrentColorThemeForm(request.POST, instance=color)
        if form.is_valid():
            form.save()

    form = CurrentColorThemeForm()

    context = {
        'color': color,
        'form': form,
    }

    return context
