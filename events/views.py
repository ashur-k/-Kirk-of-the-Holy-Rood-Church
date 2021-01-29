from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import Events
from .forms import EventsForm
from django.contrib import messages


def events(request):
    events = Events.objects.filter(event_display_status=True)
    event_form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have succesfully updated the page!')
            return redirect(reverse('events'))
        else:
            print(form.errors)
            messages.error(
                request,
                'Editing events content is failed for errors in form!')
            return redirect(reverse('events'))
    context = {
         'events': events,
         'event_form': event_form,
        }
    template = 'events/events.html'
    return render(request, template, context)


def edit_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have succesfully updated the page!')
            return redirect(reverse('events'))
        else:
            print(form.errors)
            messages.error(
                request,
                'Editing events content is failed for errors in form!')
            return redirect(reverse('events'))
