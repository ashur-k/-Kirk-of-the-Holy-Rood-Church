from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import JsonResponse
from .models import Ministries, MeetingTimes, WeekDays

from .forms import (
    MessageForm,
    MinistrieForm,
    AddMeetingTimesForm,
)
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def _send_confirmation_email(form, cust_email):
    """
        Send the user a confirmation email
    """
    cust_email = cust_email
    subject = render_to_string(
        'ministries/confirmation_emails/confirmation_email_subject.txt',
        {'form': form}
        )
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


def ministry(request, id):
    ministry = get_object_or_404(Ministries, id=id)
    times = MeetingTimes.objects.filter(meeting_ministry_name=ministry.id)
    meeting_days = WeekDays.objects.filter()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.ministy = ministry
            form.save()
            cust_email = ministry.group_leader_email
            _send_confirmation_email(form, cust_email)
            messages.success(request, 'We have received your inforamtion, thanks and we will contact you soon!')
        else:
            messages.error(request, 'Please enter valid information.')

    form = MessageForm()
    time_form = AddMeetingTimesForm()
    template = 'ministries/ministry.html'
    context = {
         'form': form,
         'ministry': ministry,
         'times': times,
         'time_form': time_form,
         'meeting_days': meeting_days,
        }

    return render(request, template, context)


def ministry_edit(request, id):

    ministry = get_object_or_404(Ministries, id=id)
    form = MinistrieForm(instance=ministry)

    if request.method == 'POST':
        form = MinistrieForm(request.POST, instance=ministry)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have succesfully updated the page!')
            return redirect(reverse('ministry', args=[ministry.id]))

    template = 'ministries/ministry_admin_edit.html'
    context = {
        'ministry': ministry,
        'form': form,
        }

    return render(request, template, context)


def add_ministry(request):
    form = MinistrieForm()

    if request.method == 'POST':
        form = MinistrieForm(request.POST)
        if form.is_valid():
            ministry = form.save()
            messages.success(request, 'New Ministry is added!')
            return redirect(reverse('ministry', args=[ministry.id]))
        else:
            print("form errors are", form.errors)
            return HttpResponse("Form is not valid")

    template = 'ministries/add_new_ministry.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


def add_new_meeting_times(request, id):
    ministry = get_object_or_404(Ministries, pk=id)
    print()
    if request.method == 'POST':
        form = AddMeetingTimesForm(request.POST)
        if form.is_valid():
            ministry_form = form.save(commit=False)
            ministry_form.meeting_ministry_name = ministry
            ministry_form.save()
            messages.success(request, "New meeting times are added")
        else:
            messages.error(request, "Add new carousel failed.")

    return redirect(reverse('ministry', args=[ministry.id]))


def delete_meeting_times(request, id):
    meeting_time = get_object_or_404(MeetingTimes, pk=id)
    ministry_id = meeting_time.meeting_ministry_name.id
    meeting_time.delete()
    messages.success(request, 'Meeting time deleted successfully!')
    return redirect(reverse('ministry', args=[ministry_id]))


def edit_meeting_times(request, id):
    meeting_time = get_object_or_404(MeetingTimes, pk=id)

    ministry_id = meeting_time.meeting_ministry_name.id

    if request.method == 'POST':
        form = AddMeetingTimesForm(request.POST, instance=meeting_time)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meeting time updated successfully!')
            return redirect(reverse('ministry', args=[ministry_id]))
        else:
            print(form.errors)
            messages.error(request, f'Please correct following.{form.errors}')
            return redirect(reverse('ministry', args=[ministry_id]))
