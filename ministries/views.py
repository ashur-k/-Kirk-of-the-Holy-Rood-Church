from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import AlphaGroup, Ministries, MeetingTimes
from .forms import AlphaGroupEntranceForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def _send_confirmation_email(form):
    """
        Send the user a confirmation email
    """
    cust_email = 'ashurkanwal@gmail.com'
    subject = render_to_string(
        'ministries/confirmation_emails/confirmation_email_subject.txt',
        {'form': form})
    body = render_to_string(
        'ministries/confirmation_emails/confirmation_email_body.txt',
        {
            'form': form,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        }
        )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


def alpha_ministry(request):
    ministry = get_object_or_404(Ministries, id=1)
    times = MeetingTimes.objects.filter(meeting_times_id=ministry.id)
    for items in times:
        print(items)

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion, thanks and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/alpha_ministry.html'
    context = {
         'form': form,
         'ministry': ministry,
         'times': times,
        }

    return render(request, template, context)


def mother_and_toddlers(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/mother_and_toddlers.html'
    context = {
         'form': form,
        }

    return render(request, template, context)


def women_association(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/women_association.html'
    context = {
         'form': form,
        }

    return render(request, template, context)


def bible_studies(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/bible_studies.html'
    context = {
         'form': form,
        }

    return render(request, template, context)


def children(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/children.html'
    context = {
         'form': form,
        }

    return render(request, template, context)


def wednesday_coffee(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/wednesday_coffee.html'
    context = {
         'form': form,
        }

    return render(request, template, context)


def gardners_group(request):

    if request.method == 'POST':
        form = AlphaGroupEntranceForm(request.POST)
        if form.is_valid():
            form = form.save()
            _send_confirmation_email(form)
            messages.success(request, 'We have received your inforamtion and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')
    form = AlphaGroupEntranceForm()
    template = 'ministries/gardners_group.html'
    context = {
         'form': form,
        }

    return render(request, template, context)