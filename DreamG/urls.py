from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from main.views import page_not_found             #импорт функции для обработки исключекния

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls')),                     #подключили все маршруты из приложения main
    path('__debug__/', include('debug_toolbar.urls')),  #подключили debug_toolbar для отладки проекта на localhost
]

handler404 = page_not_found                       #обработчик исключения handler404 и ссылка на функцию представления page_not_found

admin.site.site_header = 'DreamG аdministration panel'   #замена заголовка в админке