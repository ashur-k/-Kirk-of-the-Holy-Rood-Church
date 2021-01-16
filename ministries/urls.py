from django.urls import path
from .import views


urlpatterns = [
    path('ministry/<name>',
         views.ministry,
         name='ministry'),

    path('ministry_edit/<int:id>/',
         views.ministry_edit,
         name='ministry_edit'),
]
