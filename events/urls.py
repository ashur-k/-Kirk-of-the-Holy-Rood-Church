from django.urls import path
from . import views


urlpatterns = [
    path('events/', views.events, name='events'),
    path('edit_event/<int:event_id>/',
         views.edit_event,
         name='edit_event'
         ),

    path('buy_event_tickets/<int:event_id>/',
         views.buy_event_tickets,
         name='buy_event_tickets'
         ),
]
