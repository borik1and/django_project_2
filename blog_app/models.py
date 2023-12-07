from django.db import models
from datetime import date

NULLABLE = {'blank': True, 'null': True}


class Blog_app(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=500, **NULLABLE, verbose_name='slug')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_app/', **NULLABLE, verbose_name='Превью')
    creation_date = models.DateField(default=date.today, verbose_name='дата создания')
    publication = models.BooleanField(default=True, verbose_name='признак публикации')
    view_num = models.IntegerField(verbose_name='количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title}{self.body}{self.creation_date}{self.publication}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

