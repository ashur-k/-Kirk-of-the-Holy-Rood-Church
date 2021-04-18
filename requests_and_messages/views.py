from django.contrib import messages
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from ministries.models import Message
from home.models import CurrentColorTheme
from home.forms import CurrentColorThemeForm


def request_and_messages(request, minstry_id=None):
    request_messages = Message.objects.filter(ministy=minstry_id)

    context = {
        "request_messages": request_messages,
    }
    template = "requests_and_messages/requests_and_messages.html"

    return render(request, template, context)


def admin_settings(request):

    # color = get_object_or_404(CurrentColorTheme, id=1)

    # if request.method == 'POST':
    #     color_theme_form = CurrentColorThemeForm(request.POST, instance=color)
    #     if color_theme_form.is_valid():
    #         color_theme_form.save()
    #         messages.success(request, 'Successfully updated theme.')
    #         return redirect(reverse('admin_settings'))

    # color_theme_form = CurrentColorThemeForm(instance=color)

    context = {
        # 'color': color,
        # 'color_theme_form': color_theme_form,
    }
    template = "requests_and_messages/admin_settings.html"

    return render(request, template, context)
