from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('carousel_text_edit/<int:id>/',
         views.carousel_text_edit,
         name='carousel_text_edit'),

    path('inner_carousel_edit/<int:id>/',
         views.inner_carousel_edit,
         name='inner_carousel_edit'),

    path('add_new_carousel/', views.add_new_carousel, name='add_new_carousel'),

    path('parallax_edit/<int:id>/',
         views.parallax_edit,
         name='parallax_edit'),

    path('study_group_edit/',
         views.study_group_edit,
         name='study_group_edit'),
]
