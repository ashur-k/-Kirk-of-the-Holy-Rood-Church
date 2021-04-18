from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from . models import Videos, SundayServiceInformation, SundayServiceBooking
from .forms import SundayServiceInformationForm, SundayServiceBookingForm, SundayServiceBooking


def services(request):
    template = 'services/videos_services.html'
    videos = Videos.objects.all()

    context = {
        'videos': videos,
        }

    return render(request, template, context)


def sunday_services(request):
    service = SundayServiceInformation.objects.all()
    template = 'services/sunday_services.html'

    form = SundayServiceInformationForm()

    context = {
        'services': service,
        'form': form
        }

    return render(request, template, context)


def sunday_service_booking(request, id):
    service = get_object_or_404(SundayServiceInformation, id=id)


    form = SundayServiceBookingForm()

    if request.method == 'POST':
        form = SundayServiceBookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.service_title = service
            form.save()
            service.update_available_bookings(booking_form.number_of_bookings)
            return redirect(reverse('sunday_services'))

    template = 'services/sunday_service_booking_form.html'

    context = {
        'service': service,
        'form': form
        }

    return render(request, template, context)


def sunday_bookings(request):

    template = 'services/sunday_services.html'

    context = {

        }

    return render(request, template, context)


def edit_sunday_services(request, id):
    service = get_object_or_404(SundayServiceInformation, id=id)
    template = 'services/edit_sunday_services.html'
    form = SundayServiceInformationForm(instance=service)

    if request.method == 'POST':
        form = SundayServiceInformationForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service information successfully updated')
            return redirect(reverse('sunday_services'))

    context = {
        'services': service,
        'form': form
        }

    return render(request, template, context)


def get_sunday_bookings(request):
    sunday_service_bookings = SundayServiceBooking.objects.all()
    template = 'services/sunday_service_bookings.html'

    context = {
        'sunday_service_bookings': sunday_service_bookings
    }

    return render(request, template, context)
