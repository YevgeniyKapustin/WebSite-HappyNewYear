from django.db import models
from django.forms import FileField


class Dog(models.Model):
    name: str = models.CharField(max_length=100, verbose_name='название')
    group: str = models.CharField(max_length=100, verbose_name='группа')
    goal: str = models.TextField(verbose_name='зачем нужна?')
    character: str = models.TextField(verbose_name='характер')
    comment: str = models.TextField(verbose_name='комментарий автора')

    main_image: FileField = models.ImageField(
        upload_to='images', verbose_name='основное изображение'
    )
    image1: FileField = models.ImageField(
        upload_to='images', verbose_name='изображение для карусели 1'
    )
    image2: FileField = models.ImageField(
        upload_to='images', verbose_name='изображение для карусели 2'
    )
    image3: FileField = models.ImageField(
        upload_to='images', verbose_name='изображение для карусели 3'
    )

    def __str__(self):
        return self.name
