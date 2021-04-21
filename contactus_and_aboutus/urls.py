from django.urls import path
from . import views


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),

]
