from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Subscription(models.Model):
    title = models.CharField('Длительность подписки', max_length=30)
    description = models.CharField('Описание', max_length=150)
    price = models.FloatField('Цена')
    image = models.ImageField('Изображение', upload_to='sub_image/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Абонимент"
        verbose_name_plural = "Абонименты"


class TvBox(models.Model):
    title = models.CharField('Название', max_length=30)
    stone = models.CharField('Процессор', max_length=30)
    video_size = models.CharField('Разрешение', max_length=30)
    graphics = models.CharField('Графика', max_length=30, blank=True)
    memory = models.CharField('Память', max_length=30)
    ports = models.CharField('Интерфейсы', max_length=30)
    wi_fi = models.CharField('WiFi', max_length=150)
    image = models.ImageField('Изображение', upload_to='box_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Приставка"
        verbose_name_plural = "Приставки"


class Channel(models.Model):
    title = models.CharField('Название', max_length=30)
    image = models.ImageField('Изображение', upload_to='tv/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"


class Contact(models.Model):
    phone = models.CharField('Телефон в формате +1234567890', max_length=30)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = "Конфигурация контактов"
        verbose_name_plural = "Конфигурация контактов"


class ContactUs(models.Model):
    massege = models.TextField('Сообщение')
    time = models.DateTimeField('Время', auto_now_add=True)
    status = models.BooleanField('Обработан', default=False)

    def __str__(self):
        return 'Связь с нами'

    class Meta:
        verbose_name = "Связь с нами"
        verbose_name_plural = "Сообщения со страницы связь с нами"


class Request(models.Model):
    name = models.CharField('Имя', max_length=30)
    email = models.CharField('Название', max_length=30)
    massage = models.TextField('Приставка и тариф')
    time = models.DateTimeField('Время', auto_now_add=True)
    status = models.BooleanField('Обработан', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на подключение'
        verbose_name_plural = 'Заявки на подключение'
