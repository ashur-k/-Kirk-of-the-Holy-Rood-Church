from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .forms import PaymentForm, TicketPaymentForm
from events.models import Events


def payment(request):

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'donation_payment_amount': request.POST['donation_payment_amount'],
        }
        form = PaymentForm(form_data)
        print("request .methond executed")
        if form.is_valid():
            form.save()
            print("form saved")
        else:
            print("save failed")

    payment_form = PaymentForm()
    template = 'payment/payment.html'
    context = {
        'payment_form': payment_form
    }

    return render(request, template, context)


def ticket_payment(request, id):
    event = get_object_or_404(Events, id=id)
    if request.method == 'POST':
        payment_form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'donation_payment_amount': request.POST['donation_payment_amount'],
        }
        ticket_form_data = {
            'event_ticket_qty': request.POST['event_ticket_qty'],
        }
        payment_form = PaymentForm(payment_form_data)
        ticket_form = TicketPaymentForm(ticket_form_data)
        if payment_form.is_valid() and ticket_form.is_valid():
            print("Form data is valid and taken in")
            payment = payment_form.save()
            ticket = ticket_form.save(commit=False)
            ticket.payment = payment
            ticket.event = event
            ticket.save()

            #ticket_payment_form.save()

        else:
            print("Form data is not valid")

    template = 'payment/buy_ticket.html'
    payment_form = PaymentForm()
    ticket_payment_form = TicketPaymentForm
    context = {
        'event': event,
        'payment_form': payment_form,
        'ticket_payment_form': ticket_payment_form
    }

    return render(request, template, context)
