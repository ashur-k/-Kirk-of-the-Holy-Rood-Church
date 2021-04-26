from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from ministries.models import Message
from home.models import CurrentColorTheme
from home.forms import CurrentColorThemeForm
from django.contrib.auth.decorators import login_required


@login_required
def request_and_messages(request, minstry_id=None):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    query = None
    request_messages = Message.objects.filter(ministy=minstry_id)
    if minstry_id:
        minstry_id = minstry_id

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('contact_us_messages'))

            queries = Q(
                full_name__icontains=query
                ) | Q(
                    email__icontains=query
                    ) | Q(
                    date__icontains=query
                    )

            request_messages = request_messages.filter(queries)
            messages.success(
                request,
                f'{request_messages.count()} results found.')

    # pagintion
    request_messages_paginator = Paginator(request_messages, 5)
    page_num = request.GET.get('page')
    page = request_messages_paginator.get_page(page_num)
    for item in page.object_list:
        print(item.ministy)

    context = {
        "minstry_id": minstry_id,
        "request_messages": request_messages,
        "page": page,
        "query": query,
    }
    template = "requests_and_messages/requests_and_messages.html"

    return render(request, template, context)


@login_required
def admin_settings(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    context = {

    }
    template = "requests_and_messages/admin_settings.html"

    return render(request, template, context)
