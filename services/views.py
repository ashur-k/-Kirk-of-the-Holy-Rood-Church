from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from . models import Videos, SundayServiceInformation, SundayServiceBooking
from .forms import SundayServiceInformationForm, SundayServiceBookingForm, SundayServiceBooking, VideoForm


def video_services(request):
    template = 'services/videos_services.html'
    title_video = get_object_or_404(Videos, pinned=True)
    if request.user.is_superuser:
        videos = Videos.objects.all()
    else:
        videos = Videos.objects.filter(status="True")

    context = {
        'title_video': title_video,
        'videos': videos,
        }

    return render(request, template, context)


def play_video(request, video_id):

    title_video = get_object_or_404(Videos, id=video_id)
    videos = Videos.objects.filter(status="True")
    template = 'services/videos_services.html'
    context = {
        'title_video': title_video,
        'videos': videos,
    }
    return render(request, template, context)


def pin_video(request, video_id):

    for video in Videos.objects.all():
        if video.pinned:
            video.unpin()
    video = get_object_or_404(Videos, pk=video_id)
    video.pin()
    return redirect('video_services')


def add_video(request):
    video_form = VideoForm()
    template = "services/add_new_video.html"

    if request.method == 'POST':
        video_form = VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            video = video_form.save(commit=False)
            if video.pinned:
                if video.status == "False":
                    messages.error(request, 'Pinned Videos visivility status is required to set true.')
                    return redirect('add_video')
                else:
                    video = video_form.save()
                    for video in Videos.objects.all():
                        video.unpin()
                    video = get_object_or_404(Videos, pk=video.id)
                    video.pin()
                    messages.success(request, 'Video is successfully added and pinned.')
                    return redirect('video_services')
            else:
                video = video_form.save()
                messages.success(request, 'Video is successfully added.')
                return redirect('video_services')
    context = {
        'video_form': video_form
    }
    return render(request, template, context)


def edit_video(request, id):
    video_obj = get_object_or_404(Videos, pk=id)
    video_pinned = video_obj.pinned

    if request.method == 'POST':
        video_form = VideoForm(request.POST, request.FILES, instance=video_obj)
        if video_form.is_valid():
            video = video_form.save(commit=False)
            if video.pinned:
                if video.status == "False":
                    messages.error(request, 'Pinned Videos visivility status is required to set true.')
                else:
                    video = video_form.save()
                    for video in Videos.objects.all():
                        video.unpin()
                    new_video = get_object_or_404(Videos, pk=video.id)
                    new_video.pin()
                    messages.success(request, 'Video is successfully updated.')
                    return redirect('video_services')
            else:
                if video_obj.pinned is False and video_pinned is True:
                    messages.error(request, 'Please do not try unpinning video')
                else:
                    video_form.save()
                    messages.success(request, 'Video is successfully updated.')
                    return redirect('video_services')


    video_form = VideoForm(instance=video_obj)
    template = "services/edit_video.html"
    context = {
        'video_form': video_form
    }
    return render(request, template, context)


def del_video(request, id):
    video = get_object_or_404(Videos, id=id)
    video.delete()
    messages.success(request, 'Video is deleted successfully!')
    return redirect(reverse('video_services'))


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
