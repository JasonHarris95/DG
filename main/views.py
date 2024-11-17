from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [{'title':'HOME', 'url_name':'home'},              #переменная-список, для передачи в словарь data меню сайта
        {'title':'GAMES', 'url_name':'games'},
        {'title':'PROJECTS', 'url_name':'projects'},
        {'title':'CONTACTS', 'url_name':'contacts'}]

def home(request):                                        #параметр запроса
    data = {'title':'DreamG | Home',
            'menu':menu}
    return render(request, 'main/home.html', context=data)

def games(request):
    data = {'title': 'DreamG | Games'}
    return render(request, 'main/games.html', context=data)

def projects(request):
    data = {'title': 'DreamG | Projects'}
    return render(request, 'main/projects.html', context=data)

def contacts(request):
    data = {'title': 'DreamG | Contacts'}
    return render(request, 'main/contacts.html', context=data)

def page_not_found(request, exception):    #(request, исключение)
    return HttpResponseNotFound('<h1>Page not found</h1>')   #объект класса HttpResponseNotFound