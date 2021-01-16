from django.shortcuts import render
from . models import Videos


def services(request):
    template = 'services/videos_services.html'
    videos = Videos.objects.all()

    context = {
        'videos': videos,
        }

    return render(request, template, context)
