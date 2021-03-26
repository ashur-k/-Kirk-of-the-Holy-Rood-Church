from django.urls import path
from .import views


urlpatterns = [
    path('', views.request_and_messages, name='request_and_messages'),

    path(
        '<int:minstry_id>/',
        views.request_and_messages,
        name='request_and_messages'),

    path('admin_settings/', views.admin_settings, name='admin_settings'),

]
