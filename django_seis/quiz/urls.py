from django.urls import path

from django.contrib import admin
from quiz import views

urlpatterns = [
    path('', views.show_index),
    path('check_response', views.check_response),
]
