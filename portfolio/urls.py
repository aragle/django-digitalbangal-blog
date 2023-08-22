# Description: This file contains the url patterns for the portfolio app.

from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.portfolio, name='Portfolio'),
]
