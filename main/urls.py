from django.urls import path
from . import views                     # . из этой же папки

urlpatterns = [
    path('', views.home, name='home'),               #путь, функция представления, имя пути
    path('games/', views.games, name='games'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
]
