from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
        verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
        verbose_name='Рубрика')
        
    class Kinds(models.IntegerChoices):
        BUY = 1, 'Куплю'
        SELL = 2, 'Продам'
        EXCHANGE = 3, 'Обменяю'
        RENT = 4
        __empty__ = 'Выберите тип публикуемого объявления'

    kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)

    class Meta:
        verbose_name_plural = 'Объявления' # название модели во множ. числе
        verbose_name = 'объявление' # название в ед. числе
        ordering = ['-published']

class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
        verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
