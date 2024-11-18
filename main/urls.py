from django.urls import path
from . import views                     # . из этой же папки

urlpatterns = [
    path('', views.home_ru, name='home_ru'),               #путь, функция представления, имя пути
    path('games_ru/', views.games_ru, name='games_ru'),
    path('projects_ru/', views.projects_ru, name='projects_ru'),
    path('contacts_ru/', views.contacts_ru, name='contacts_ru'),
    path('en/', views.home, name='home'),
    path('games/', views.games, name='games'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
]
