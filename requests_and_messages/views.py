from django.shortcuts import render, HttpResponse
from ministries.models import Message


def request_and_messages(request, minstry_id=None):
    request_messages = Message.objects.filter(ministy=minstry_id)

    context = {
        "request_messages": request_messages,
    }
    template = "requests_and_messages/requests_and_messages.html"

    return render(request, template, context)


def admin_settings(request):

    context = {
        "request_messages": 'request_messages',
    }
    template = "requests_and_messages/admin_settings.html"

    return render(request, template, context)
