from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pokemon/<int:number>/', views.pokemon, name="pokemon"),
    path('AddPokemon/<int:id>/', views.AddPokemon, name="AddPokemon"),
    path('GetSessionTeam/', views.GetSessionTeam, name="GetSessionTeam")
]