from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from . models import Events
from .forms import EventsForm
from payment.forms import PaymentForm, TicketPaymentForm
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
            return render(request, 'events/event_payment_page.html', {
                    'payment_form': payment_form,
                    'ticket_payment_form': ticket_form,
                }
                )
    payment_form = PaymentForm()
    ticket_payment_form = TicketPaymentForm
    template = 'events/event_payment_page.html'
    context = {
        'event': event,
        'payment_form': payment_form,
        'ticket_payment_form': ticket_payment_form,
    }

    return render(request, template, context)
