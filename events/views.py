from django.shortcuts import render
from . models import Events


def events(request):
    events = Events.objects.filter(event_display_status=True)
    context = {
         'events': events
        }
    template = 'events/events.html'
    return render(request, template, context)
