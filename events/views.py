from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse)
from . models import Events, EventDates, BookingFreeEvents
from .forms import EventsForm, EventDateForm, BookingFreeEventsForm
from payment.forms import PaymentForm, TicketPaymentForm
from django.contrib import messages


def events(request):
    events = Events.objects.filter(event_display_status=True)
    event_form = EventsForm()
    event_date_form = EventDateForm()

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
         'event_date_form': event_date_form,
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


def delete_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    event.delete()
    messages.success(request, 'Succesfully deleted an event!')
    return redirect(reverse('events'))


def add_event_date_time(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.method == 'POST':
        form = EventDateForm(request.POST)
        if form.is_valid():
            event_date_form = form.save(commit=False)
            event_date_form.event = event
            form.save()
            messages.success(request, 'You have succesfully updated the page!')
            return redirect(reverse('events'))
        return HttpResponse(form.errors)


def edit_event_date_time(request, event_date_time_id):
    event_date_time = get_object_or_404(EventDates, id=event_date_time_id)

    if request.method == 'POST':
        form = EventDateForm(request.POST, instance=event_date_time)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have succesfully edited the event date-time!')
            return redirect(reverse('events'))
        return HttpResponse(form.errors)


def delete_event_date_time(request, event_date_time_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Church Admin can watch this.')
        return redirect(reverse('home'))

    event_date_time = get_object_or_404(EventDates, id=event_date_time_id)
    event_date_time.delete()
    messages.success(request, 'event_date_time deleted!')
    return redirect(reverse('events'))


def buy_event_tickets(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.method == 'POST':

        payment_form = PaymentForm(request.POST)
        ticket_form = TicketPaymentForm(request.POST)
        if payment_form.is_valid() and ticket_form.is_valid():
            payment_bag = request.session.get('payment_bag', {})
            payment_bag['full_name'] = request.POST.get('full_name')
            payment_bag['email'] = request.POST.get('email')
            payment_bag['phone_number'] = request.POST.get('phone_number')
            payment_bag['donation_payment_amount'] = request.POST.get(
                'donation_payment_amount')

            payment_bag['event_date'] = request.POST.get('event_date')
            payment_bag['ticket_qty'] = request.POST.get(
                'event_ticket_qty')
            payment_bag['donation_page'] = False
            donation_amount = request.POST.get('donation_payment_amount')
            ticket_qty = int(request.POST.get('event_ticket_qty'))
            event_price = event.event_price

            event_total = ticket_qty * event_price
            total_amount = int(donation_amount) + event_total
            payment_bag['total_amount'] = int(total_amount)
            payment_bag['event_id'] = event_id
            request.session['payment_bag'] = payment_bag

            return redirect(reverse('ticket_payment', args=[event.id]))
        else:
            ash = payment_form.errors
            bsh = ticket_form.errors
            print(bsh, ash)
            return HttpResponse(bsh)

    payment_form = PaymentForm()
    ticket_payment_form = TicketPaymentForm
    template = 'events/event_payment_page.html'
    context = {
        'event': event,
        'payment_form': payment_form,
        'ticket_payment_form': ticket_payment_form,
    }

    return render(request, template, context)


def booking_free_event(request, event_id):

    event = get_object_or_404(Events, id=event_id)
    event_dates = EventDates.objects.filter(event=event_id)

    if request.method == 'POST':
        event_booking_date = request.POST['event_booking_date']
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'number_of_bookings': request.POST['number_of_bookings'],
        }
        booking_free_event_form = BookingFreeEventsForm(form_data)
        if booking_free_event_form.is_valid():
            booking_free_event = booking_free_event_form.save(commit=False)
            booking_free_event.event_title = event
            booking_free_event.event_booking_date = event_booking_date
            booking_free_event = booking_free_event_form.save()

            bookings = booking_free_event.number_of_bookings

            # updating event ticket count
          
            messages.success(request, 'You haeve successfully booked for this event.')
            return redirect(reverse('free_event_booking_success', args=[booking_free_event.id]))

    booking_free_event_form = BookingFreeEventsForm()
    template = 'events/booking_free_event.html'

    context = {
        'event_dates': event_dates,
        'free_event_form': booking_free_event_form,
    }
    return render(request, template, context)


def free_event_booking_success(request, id):

    booked_event_data = get_object_or_404(BookingFreeEvents, id=id)
    event_id = booked_event_data.event_title.id
    event = get_object_or_404(Events, id=event_id)

    template = 'events/event_booking_success.html'

    context = {
        'event': event,
        'booked_event_data': booked_event_data,
    }
    return render(request, template, context)
