from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Message, Ministries, MeetingTimes
from .forms import MessageForm, MinistrieForm
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


def ministry(request, name):
    ministry = get_object_or_404(Ministries, ministry_heading=name)
    times = MeetingTimes.objects.filter(meeting_times_id=ministry.id)

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
    template = 'ministries/ministry.html'
    context = {
         'form': form,
         'ministry': ministry,
         'times': times,
        }

    return render(request, template, context)


def ministry_edit(request, id):

    ministry = get_object_or_404(Ministries, id=id)
    times = MeetingTimes.objects.filter(meeting_times_id=ministry.id)
    form = MinistrieForm(instance=ministry)

    template = 'ministries/ministry_admin_edit.html'
    context = {
        'ministry': ministry,
        'times': times,
        'form': form,
        }

    return render(request, template, context)
