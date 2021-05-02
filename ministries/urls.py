from django.urls import path
from .import views


urlpatterns = [
    path('ministry/<int:ministry_id>/',
         views.ministry,
         name='ministry'),

    path('ministry_edit/<int:id>/',
         views.ministry_edit,
         name='ministry_edit'),

    path('add_ministry/',
         views.add_ministry,
         name='add_ministry'),

    path('add_new_meeting_times/<int:id>/',
         views.add_new_meeting_times,
         name='add_new_meeting_times'),

    path('delete_meeting_times/<int:id>/',
         views.delete_meeting_times,
         name='delete_meeting_times'),

    path('edit_meeting_times/<int:id>/',
         views.edit_meeting_times,
         name='edit_meeting_times'),
]
