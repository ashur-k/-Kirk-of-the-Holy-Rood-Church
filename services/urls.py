from django.urls import path
from .import views


urlpatterns = [
    path('services/', views.services, name='services'),
    path('sunday_services/', views.sunday_services, name='sunday_services'),
]
