from django.urls import path
from .import views


urlpatterns = [
    path('mother_and_toddlers/',
         views.mother_and_toddlers,
         name='mother_and_toddlers'),

    path('women_association/',
         views.women_association,
         name='women_association'),

    path('alpha_ministry/',
         views.alpha_ministry,
         name='alpha_ministry'),

    path('bible_studies/',
         views.bible_studies,
         name='bible_studies'),

    path('children/',
         views.children,
         name='children'),

    path('wednesday_coffee/',
         views.wednesday_coffee,
         name='wednesday_coffee'),

    path('gardners_group/',
         views.gardners_group,
         name='gardners_group'),

]
