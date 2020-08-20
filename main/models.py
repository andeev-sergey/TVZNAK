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
