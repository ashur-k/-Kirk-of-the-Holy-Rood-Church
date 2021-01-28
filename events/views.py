from django.shortcuts import render
from . models import Events
from .forms import EventsForm, EventForm


def events(request):
    events = Events.objects.filter(event_display_status=True)
    event_form = EventForm()

    context = {
         'events': events,
         'event_form': event_form,
        }
    template = 'events/events.html'
    return render(request, template, context)
