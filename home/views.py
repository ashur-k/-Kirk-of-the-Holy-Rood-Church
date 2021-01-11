from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import HeroSectionText
from .forms import HeroSectionTextForm
from django.contrib import messages


def index(request):
    """ A view to return the undex page """
    hero_heading = get_object_or_404(HeroSectionText, id=1)

    if request.user.is_superuser:
        form = HeroSectionTextForm(instance=hero_heading)
        if request.method == 'POST':
            form = HeroSectionTextForm(request.POST, instance=hero_heading)
            if form.is_valid():
                form.save()
                messages.success(request, 'Text updated successfully.')
        context = {
            'form': form,
            'hero_heading': hero_heading,
        }
    else:
        context = {
            'hero_heading': hero_heading,
        }
    template = 'home/index.html'
    return render(request, template, context)
