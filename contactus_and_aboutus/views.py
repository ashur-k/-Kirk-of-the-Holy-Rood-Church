from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import Contactus
from .forms import ContactusForm
from ministries.views import _send_confirmation_email
from django.contrib.auth.decorators import login_required


def contact_us(request):

    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            form_obj = form.save()
            cust_email = form_obj.send_email_to
            _send_confirmation_email(form_obj, cust_email)

            ''' Creating boolean variable to check
                if Home page Form is used to send message.
            '''
            from_home_page = bool(request.POST.get('from_home_page'))

            # Returning back to Home Page
            if from_home_page is True:
                messages.success(
                    request,
                    f'Hello {form_obj.full_name}, your message is received and we will contact you soon.')
                return redirect(reverse('home'))
            else:
                # Returning back to Contact Us page
                messages.success(
                    request,
                    f'Hello {form_obj.full_name}, your message is received and we will contact you soon.')
                return redirect(reverse('contact-us'))

    form = ContactusForm
    template = 'contactus_and_aboutus/contact-us.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def contact_us_messages(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    contact_us_messages = Contactus.objects.all().order_by('-id')
    query = None
    # query = request.GET['q']

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('contact_us_messages'))

            queries = Q(
                full_name__icontains=query
                ) | Q(
                    receieve_at__icontains=query
                    )

            contact_us_messages = contact_us_messages.filter(queries)
            messages.success(
                request,
                f'{contact_us_messages.count()} results found.')

    # pagintion
    contactus_messages_paginator = Paginator(contact_us_messages, 5)
    page_num = request.GET.get('page')
    page = contactus_messages_paginator.get_page(page_num)

    template = 'contactus_and_aboutus/contact-us-messages.html'
    context = {
        'count': contactus_messages_paginator.count,
        'page': page,
        'query': query
    }

    return render(request, template, context)


@login_required
def del_contactus_msgs(request, id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    message = get_object_or_404(Contactus, id=id)
    message_name = message.full_name
    message.delete()
    messages.success(
                request,
                f'Message from {message_name} is succesfully deleted.')
    return redirect(reverse('contact_us_messages'))


def about_us(request):
    template = 'contactus_and_aboutus/about-us.html'
    context = {

    }
    return render(request, template, context)
