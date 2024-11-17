from django.contrib import admin
from .models import Main

class MainAdmin(admin.ModelAdmin):                                 #поля класса должны быть либо списком, либо кортежем
    list_display = ('id','title', 'time_create', 'isPublished')    #кортеж полей для отображения в админке
    list_display_links = ('id','title')                            #указание кортежа полей, по которым будет открываться статья
    ordering = ('time_create','title')                             #кортеж полей, по которым будет сортировка
    list_per_page = 25                                             #пагинация списка
    search_fields = ('title',)                                     #добавление поля поиска

admin.site.register(Main, MainAdmin)
