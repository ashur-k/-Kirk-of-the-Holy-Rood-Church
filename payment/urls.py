from django.urls import path
from .import views


urlpatterns = [
   path('payment/', views.payment, name='payment'),
   path('ticket_payment/<int:id>/', views.ticket_payment, name='ticket_payment'),

]
