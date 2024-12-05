from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

current_version = 'Current version: V.05.02'                            #для передачи в шаблоны {{ }}
current_version_ru = 'Текущая версия: V.05.02'

rights_reserved = '© 2024 DreamG. All rights reserved.'
rights_reserved_ru = '© 2024 DreamG. Все права защищены.'

was_developed = 'The site was developed with love by Just Web team'
was_developed_ru = 'Сайт был разработан с любовью командой Just Web'

def home_ru(request):                                        #параметр запроса
    data = {'title':'DreamG | Главная',
            'rights_reserved': rights_reserved_ru,
            'was_developed': was_developed_ru,
            'current_version': current_version_ru}
    return render(request, 'main/home_ru.html', context=data)

def games_ru(request):
    data = {'title': 'DreamG | Игры',
            'rights_reserved': rights_reserved_ru,
            'was_developed': was_developed_ru,
            'current_version': current_version_ru}
    return render(request, 'main/games_ru.html', context=data)

def projects_ru(request):
    data = {'title': 'DreamG | Другие проекты',
            'rights_reserved': rights_reserved_ru,
            'was_developed': was_developed_ru,
            'current_version': current_version_ru}
    return render(request, 'main/projects_ru.html', context=data)

def contacts_ru(request):
    data = {'title': 'DreamG | Контакты',
            'rights_reserved': rights_reserved_ru,
            'was_developed': was_developed_ru,
            'current_version': current_version_ru}
    return render(request, 'main/contacts_ru.html', context=data)

def home(request):                                        #параметр запроса
    data = {'title':'DreamG | Home',
            'rights_reserved': rights_reserved,
            'was_developed': was_developed,
            'current_version': current_version}
    return render(request, 'main/home.html', context=data)

def games(request):
    data = {'title': 'DreamG | Games',
            'rights_reserved': rights_reserved,
            'was_developed': was_developed,
            'current_version': current_version}
    return render(request, 'main/games.html', context=data)

def projects(request):
    data = {'title': 'DreamG | Other projects',
            'rights_reserved': rights_reserved,
            'was_developed': was_developed,
            'current_version': current_version}
    return render(request, 'main/projects.html', context=data)

def contacts(request):
    data = {'title': 'DreamG | Contacts',
            'rights_reserved': rights_reserved,
            'was_developed': was_developed,
            'current_version': current_version}
    return render(request, 'main/contacts.html', context=data)

def page_not_found(request, exception):    #(request, исключение)
    return HttpResponseNotFound('<h1>Page not found</h1>')   #объект класса HttpResponseNotFound