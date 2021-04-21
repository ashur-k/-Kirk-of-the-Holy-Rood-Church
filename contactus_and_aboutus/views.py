from django.shortcuts import render, HttpResponse


def contact_us(request):
    template = 'contactus_and_aboutus/contact-us.html'
    context = {

    }
    return render(request, template, context)


def about_us(request):
    template = 'contactus_and_aboutus/about-us.html'
    context = {

    }
    return render(request, template, context)
