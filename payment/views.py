from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .forms import PaymentForm, TicketPaymentForm
from events.models import Events
import stripe
from django.conf import settings


def payment(request):

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'donation_payment_amount': request.POST['donation_payment_amount'],
        }
        form = PaymentForm(form_data)
        if form.is_valid():
            payment_bag = request.session.get('payment_bag', {})
            payment_bag['full_name'] = request.POST.get('full_name')
            payment_bag['email'] = request.POST.get('email')
            payment_bag['phone_number'] = request.POST.get('phone_number')
            payment_bag['donation_payment_amount'] = request.POST.get(
                'donation_payment_amount')
            payment_bag['donation_page'] = True
            payment_bag['total_amount'] = request.POST.get(
                'donation_payment_amount')
            request.session['payment_bag'] = payment_bag
            return redirect(reverse('ticket_payment', args=[1]))
        else:
            print("save failed payment.view line 20")

    payment_form = PaymentForm()
    template = 'payment/payment.html'
    context = {
        'payment_form': payment_form,
    }

    return render(request, template, context)


def ticket_payment(request, id):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    event = get_object_or_404(Events, id=id)
    payment_bag = request.session.get('payment_bag')
    from_donation_page = (payment_bag['donation_page'])

    """ This part is calculating stripe payment total
        taking value from session and assigning it to form
    """
    # donation_price = int(payment_bag['donation_payment_amount'])
    # ticket_qty = int(payment_bag['ticket_qty'])
    # event_price = event.event_price
    # total_amount = donation_price + ticket_qty * event_price
    total_amount = payment_bag['total_amount']
    stripe_payment = int(total_amount)

    if request.method == 'POST':
        if from_donation_page:
            payment_form_data = {
                'full_name': payment_bag['full_name'],
                'email': payment_bag['email'],
                'phone_number': payment_bag['phone_number'],
                'donation_payment_amount': payment_bag['donation_payment_amount'],
                }
            payment_form = PaymentForm(payment_form_data)
            if payment_form.is_valid():
                payment = payment_form.save()
        else:
            payment_form_data = {
                'full_name': payment_bag['full_name'],
                'email': payment_bag['email'],
                'phone_number': payment_bag['phone_number'],
                'donation_payment_amount': payment_bag['donation_payment_amount'],
                }
            ticket_form_data = {
                'event_ticket_qty': payment_bag['ticket_qty'],
            }
            payment_form = PaymentForm(payment_form_data)
            ticket_form = TicketPaymentForm(ticket_form_data)
            if payment_form.is_valid() and ticket_form.is_valid():
                payment = payment_form.save()

                ticket = ticket_form.save(commit=False)
                ticket.payment = payment
                ticket.event = event
                ticket.save()
            # stripe_payment = payment.grand_total

    stripe_total = round(stripe_payment * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    payment_form = PaymentForm()
    ticket_payment_form = TicketPaymentForm

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to add it in your environment?')

    template = 'payment/buy_ticket.html'
    context = {
        'event': event,
        'payment_form': payment_form,
        'ticket_payment_form': ticket_payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
