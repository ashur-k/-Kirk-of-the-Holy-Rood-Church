from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import CurrentColorTheme
from .forms import CurrentColorThemeForm
from django.contrib import messages


def site_settings(request):
    color = get_object_or_404(CurrentColorTheme, id=1)
    if request.method == 'POST':
        form = CurrentColorThemeForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated theme.')

    form = CurrentColorThemeForm(instance=color)

    context = {
        'color': color,
        'form': form,
    }

    return context
