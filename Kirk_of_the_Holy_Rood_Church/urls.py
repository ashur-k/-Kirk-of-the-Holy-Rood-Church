"""Kirk_of_the_Holy_Rood_Church URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('', include('services.urls')),
    path('', include('ministries.urls')),
    path('', include('events.urls')),
    path('', include('payment.urls')),
    path('notices/', include('notices.urls')),
    path('requests_and_messages/', include('requests_and_messages.urls')),
    path('', include('contactus_and_aboutus.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
