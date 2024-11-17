from dataclasses import field

from django.db import models
from django.db.models import Model
from django.template.defaultfilters import title


class Main(models.Model):    #наследование от models превращает наш класс в класс модели

    #дальше прописываются поля модели
    title = models.CharField(max_length=50)               #Charfield-текстовое поле (max-длина)
    content = models.TextField(blank=True)                #TextField-текст (может быть пустым)
    time_create = models.DateTimeField(auto_now_add=True) #Поля дат со временем (автозаполнение времени сейчас только при создании записи)
    time_update = models.DateTimeField(auto_now=True)                           #(при обновлении записи тоже)
    isPublished = models.BooleanField(default=True)       #Булево поле (по умолчанию = да)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]