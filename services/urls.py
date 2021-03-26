from django.urls import path
from .import views


urlpatterns = [
    path('services/', views.services, name='services'),
    path('sunday_services/', views.sunday_services, name='sunday_services'),
    path(
        'edit_sunday_services/<int:id>/',
        views.edit_sunday_services,
        name='edit_sunday_services'),
]
