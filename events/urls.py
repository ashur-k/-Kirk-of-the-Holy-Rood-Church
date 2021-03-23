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

    path('add_event_date_time/<int:event_id>/',
         views.add_event_date_time,
         name='add_event_date_time'
         ),

    path('edit_event_date_time/<int:event_date_time_id>/',
         views.edit_event_date_time,
         name='edit_event_date_time'
         ),

    path('delete_event_date_time/<int:event_date_time_id>/',
         views.delete_event_date_time,
         name='delete_event_date_time'
         ),
]
