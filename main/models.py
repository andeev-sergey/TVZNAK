from django.db import models


# Create your models here.
class Subscription(models.Model):
    title = models.CharField('Длительность подписки', max_length=30)
    description = models.CharField('Описание', max_length=150)
    price = models.IntegerField('Цена')
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
    graphics = models.CharField('Графика', max_length=30)
    memory = models.CharField('Память', max_length=30)
    ports = models.CharField('Интерфейсы', max_length=30)
    wi_fi = models.CharField('WiFi', max_length=150)
    image = models.ImageField('Изображение', upload_to='box_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Приставка"
        verbose_name_plural = "Приставки"


class Contact(models.Model):
    phone = models.CharField('Телефон в формате +1234567890', max_length=30)
    email = models.EmailField('Email', max_length=100)