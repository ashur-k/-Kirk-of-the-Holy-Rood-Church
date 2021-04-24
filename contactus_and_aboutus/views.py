from django.contrib import messages
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import Contactus
from .forms import ContactusForm


def contact_us(request):

    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            form_obj = form.save()
            messages.success(
                request,
                f'Hello {form_obj.name}, we have received your message and we will contact you soon.')

    form = ContactusForm
    template = 'contactus_and_aboutus/contact-us.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def contact_us_messages(request):

    contact_us_messages = Contactus.objects.all()

    template = 'contactus_and_aboutus/contact-us-messages.html'
    context = {
        'contact_us_messages': contact_us_messages,
    }
    return render(request, template, context)


def del_contactus_msgs(request, id):

    message = get_object_or_404(Contactus, id=id)
    message_name = message.name
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
