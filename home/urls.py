from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('carousel_text_edit/',
         views.carousel_text_edit,
         name='carousel_text_edit'),

    path('inner_carousel_edit/<int:id>/',
         views.inner_carousel_edit,
         name='inner_carousel_edit'),

    path('add_new_carousel/', views.add_new_carousel, name='add_new_carousel'),

    path('second_parallax_edit/',
         views.second_parallax_edit,
         name='second_parallax_edit'),
]
