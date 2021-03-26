from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import Videos, SundayServiceInformation
from .forms import SundayServiceInformationForm


def services(request):
    template = 'services/videos_services.html'
    videos = Videos.objects.all()

    context = {
        'videos': videos,
        }

    return render(request, template, context)


def sunday_services(request):
    service = SundayServiceInformation.objects.all()
    template = 'services/sunday_services.html'

    form = SundayServiceInformationForm()

    context = {
        'services': service,
        'form': form
        }

    return render(request, template, context)


def edit_sunday_services(request, id):
    service = get_object_or_404(SundayServiceInformation, id=id)
    template = 'services/edit_sunday_services.html'
    form = SundayServiceInformationForm(instance=service)

    if request.method == 'POST':
        form = SundayServiceInformationForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service successfully updated')
            return redirect(reverse('sunday_services'))

    context = {
        'services': service,
        'form': form
        }

    return render(request, template, context)
