from django.urls import path
from . import views


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact-us'),

    path(
        'contact_us_messages/',
        views.contact_us_messages,
        name='contact_us_messages'
    ),

    path(
        'del_contactus_msgs/<int:id>/',
        views.del_contactus_msgs,
        name='del_contactus_msgs'
    ),

    path('about-us/', views.about_us, name='about-us'),

]
