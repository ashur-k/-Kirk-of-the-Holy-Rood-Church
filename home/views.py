from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import CurrentColorTheme
from .forms import CurrentColorThemeForm


def index(request):
    """ A view to return the undex page """

    template = 'home/index.html'

    return render(request, template)
