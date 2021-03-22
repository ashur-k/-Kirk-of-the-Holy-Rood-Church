from django.urls import path
from .import views


urlpatterns = [
   path('payment/', views.payment, name='payment'),

   path(
       'ticket_payment/<int:id>/',
       views.ticket_payment,
       name='ticket_payment'),

   path(
       'payment_success/<payment_number>/',
       views.payment_success,
       name='payment_success'),

]
