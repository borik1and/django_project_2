from django.db import models
from django.utils.datetime_safe import date


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='product_app/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price_one = models.IntegerField(verbose_name='цена за штуку')
    date_add = models.DateField(default=date.today, verbose_name='дата создания')
    modified_date = models.DateField(default=date.today, verbose_name='дата последнего изменения')
    owner = models.CharField(max_length=100, default=None, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_active_version(self):
        return self.versions.filter(version_flag=True).first()


class Version(models.Model):
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_num = models.IntegerField(verbose_name='Номер версии')
    version_flag = models.BooleanField(default=True, verbose_name='Признак текущей версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='versions')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
