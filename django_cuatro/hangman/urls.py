
from django.contrib import admin
from django.urls import path, include
from hangman import views

urlpatterns = [
    path('', views.index_funcion),
    path('game_turn', views.game_turn),
]
