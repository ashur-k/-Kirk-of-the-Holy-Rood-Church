from django.urls import path
from .import views


urlpatterns = [
    path('', views.notices, name='notices'),
    path('add_new_notice/', views.add_new_notice, name='add_new_notice'),

    path(
       'edit_notice/<int:notice_id>/',
       views.edit_notice,
       name='edit_notice'),

    path(
        'delete_notice/<int:notice_id>/',
        views.delete_notice,
        name='delete_notice'),

    path(
        'add_new_newsletter/',
        views.add_new_newsletter,
        name='add_new_newsletter'),
]
