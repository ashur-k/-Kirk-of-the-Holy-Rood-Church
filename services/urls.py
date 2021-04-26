from django.urls import path
from .import views


urlpatterns = [
    path('video_services/', views.video_services, name='video_services'),
    path('all_videos/', views.all_videos, name='all_videos'),
    path('pin_video/<int:video_id>/', views.pin_video, name='pin_video'),
    path('add_video/', views.add_video, name='add_video'),
    path('edit_video/<int:id>/', views.edit_video, name="edit_video"),
    path('del_video/<int:id>/', views.del_video, name="del_video"),
    path('play_video/<int:video_id>/', views.play_video, name="play_video"),

    path('sunday_services/', views.sunday_services, name='sunday_services'),
    path(
        'edit_sunday_services/<int:id>/',
        views.edit_sunday_services,
        name='edit_sunday_services'),

    path(
        'get_sunday_bookings/',
        views.get_sunday_bookings,
        name='sunday_bookings'),

    path(
        'sunday_service_booking/<int:id>/',
        views.sunday_service_booking,
        name='sunday_service_booking'),

    path(
        'edit_sunday_booking/<int:booking_id>/',
        views.edit_sunday_booking,
        name='edit_sunday_booking'),

    path(
        'del_sunday_booking/<int:booking_id>/',
        views.del_sunday_booking,
        name='del_sunday_booking'),

    path(
        'del_all_sunday_booking/',
        views.del_all_sunday_booking,
        name='del_all_sunday_booking'),
]
