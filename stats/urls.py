# Description: URL Configuration for stats app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Stats'),
]
