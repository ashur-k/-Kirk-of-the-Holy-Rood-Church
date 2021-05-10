from decimal import Decimal
from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404)
from django.contrib import messages
from .forms import PaymentForm, TicketPaymentForm
from events.models import Events, EventDates
from .models import Payment, TicketsPayment
import stripe
from django.conf import settings
# Importing sending email functionality
from ministries.views import _send_confirmation_email


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
            print("save failed payment.view line 33")

    payment_form = PaymentForm()
    template = 'payment/payment.html'
    context = {
        'payment_form': payment_form,
    }

    return render(request, template, context)


def ticket_payment(request, event_id):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    event = get_object_or_404(Events, id=event_id)
    # Getting event_id for template
    event_id = event.id

    payment_bag = request.session.get('payment_bag')
    from_donation_page = (payment_bag['donation_page'])

    '''
        This part of code is written to set logic of template
        to be able to print different values when event or when
        doantion
    '''
    event_date = None
    donation = None
    if from_donation_page:
        # Setting event to none: if donation page then not to show event data
        event = None
        donation = payment_bag['donation_payment_amount']
    else:
        date_id = payment_bag['event_date_id']
        event_date = get_object_or_404(EventDates, id=date_id)

    """ This part is calculating stripe payment total
        taking value from session and assigning it to form
    """
    total_amount = payment_bag['total_amount']
    stripe_payment = round(float(total_amount), 2)

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

                # Sending email to person who booked event
                form = {
                    'donation_page': True,
                    'full_name': payment.full_name,
                    'phone_number': payment.phone_number,
                    'email': payment.phone_number,
                    'create_at': payment.create_at,
                    'donation_paid': payment.donation_payment_amount,
                }
                cust_email = payment.email
                _send_confirmation_email(form, cust_email)
                # Saving Full name to show on site message
                full_name = payment.full_name
                messages.success(
                    request,
                    f'Dear {full_name}, thanks for your donation.')
                return redirect(reverse(
                    'donation_success',
                    args=[payment.payment_number]))
            else:
                return HttpResponse('There is an error call Admin')
        else:
            payment_form_data = {
                'full_name': payment_bag['full_name'],
                'email': payment_bag['email'],
                'phone_number': payment_bag['phone_number'],
                'donation_payment_amount': payment_bag['donation_payment_amount'],
                }
            ticket_form_data = {
                'event_date': payment_bag['event_date'],
                'event_ticket_qty': payment_bag['ticket_qty'],
            }
            payment_form = PaymentForm(payment_form_data)
            ticket_form = TicketPaymentForm(ticket_form_data)

            if payment_form.is_valid() and ticket_form.is_valid():
                payment = payment_form.save()
                ticket_obj = ticket_form.save(commit=False)
                ticket_obj.payment = payment
                ticket_obj.event = event
                ticket_obj = ticket_form.save()

                # updating event ticket count
                event__date_id = payment_bag['event_date_id']
                event_date = get_object_or_404(EventDates, id=event__date_id)
                event_date.update_tickets_sold(
                    ticket_obj.event_ticket_qty
                    )

                # Sending email to person who booked event
                form = {
                    'full_name': payment.full_name,
                    'phone_number': payment.phone_number,
                    'email': payment.email,
                    'event_title': ticket_obj.event,
                    'event_booking_date': ticket_obj.event_date,
                    'number_of_bookings': ticket_obj.event_ticket_qty,
                    'create_at': payment.create_at,
                    'donation_paid': payment.donation_payment_amount,
                    'event_booking_payment': payment.ticket_payment_total,
                    'total_amount_paid': payment.grand_total,
                }
                cust_email = payment.email
                _send_confirmation_email(form, cust_email)

                # Saving Full name to show on site message
                full_name = payment.full_name
                messages.success(
                    request,
                    f'Dear {full_name}, have successfully booked for this event.')
                return redirect(reverse(
                    'payment_success',
                    args=[payment.payment_number]))
            else:
                return HttpResponse('Data is not in ticket payment view')
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
        'stripe_payment': stripe_payment,
        'donation': donation,
        'event_date': event_date,
        'event_id': event_id,
        'event': event,
        'payment_form': payment_form,
        'ticket_payment_form': ticket_payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def payment_success(request, payment_number):

    payment = get_object_or_404(Payment, payment_number=payment_number)
    ticket_payment = TicketsPayment.objects.filter(payment=payment.id)

    ticket_obj = get_object_or_404(
        TicketsPayment, id=ticket_payment[0].id
        )
    event = get_object_or_404(Events, id=ticket_obj.event.id)

    if payment.donation_payment_amount:
        donation = True
    else:
        donation = False

    if 'payment_bag' in request.session:
        del request.session['payment_bag']

    template = 'payment/payment_success.html'
    context = {
        'event': event,
        'payment': payment,
        'ticket': ticket_obj,
        'donation': donation
    }

    return render(request, template, context)


# this view still has work to
def donation_success(request, payment_number):

    payment = get_object_or_404(Payment, payment_number=payment_number)

    if 'payment_bag' in request.session:
        del request.session['payment_bag']


    template = 'payment/donation.succes.html'
    context = {
        'payment': payment,
    }


    return render(request, template, context)
