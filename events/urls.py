from django.urls import path
from . import views


urlpatterns = [
    path('events/', views.events, name='events'),
    path('edit_event/<int:event_id>/',
         views.edit_event,
         name='edit_event'),
]
