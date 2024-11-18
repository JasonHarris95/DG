from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu_ru = [{'title':'ГЛАВНАЯ', 'url_name':'home_ru'},        #переменная-список, для передачи в словарь data меню сайта
        {'title':'ИГРЫ', 'url_name':'games_ru'},
        {'title':'ДРУГИЕ ПРОЕКТЫ', 'url_name':'projects_ru'},
        {'title':'КОНТАКТЫ', 'url_name':'contacts_ru'}]

menu_en = [{'title':'HOME', 'url_name':'home'},              #переменная-список, для передачи в словарь data меню сайта
        {'title':'GAMES', 'url_name':'games'},
        {'title':'OTHER PROJECTS', 'url_name':'projects'},
        {'title':'CONTACTS', 'url_name':'contacts'}]

def home_ru(request):                                        #параметр запроса
    data = {'title':'DreamG | Главная',
            'menu':menu_ru}
    return render(request, 'main/home_ru.html', context=data)

def games_ru(request):
    data = {'title': 'DreamG | Игры'}
    return render(request, 'main/games_ru.html', context=data)

def projects_ru(request):
    data = {'title': 'DreamG | Другие проекты'}
    return render(request, 'main/projects_ru.html', context=data)

def contacts_ru(request):
    data = {'title': 'DreamG | Контакты'}
    return render(request, 'main/contacts_ru.html', context=data)

def home(request):                                        #параметр запроса
    data = {'title':'DreamG | Home',
            'menu':menu_en}
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