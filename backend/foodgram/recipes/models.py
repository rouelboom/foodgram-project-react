from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from multiselectfield import MultiSelectField

User = get_user_model()

# Возможные варианты выбора для поля tags
TAG_CHOICES = (('breakfast', 'Завтрак'),
               ('lunch', 'Обед'),
               ('dinner', 'Ужин'))


class Ingredient(models.Model):
    """Ингредиенты"""
    title = models.CharField(max_length=150,
                             verbose_name='Название ингредиента')
    measure = models.CharField(max_length=25,
                               verbose_name='Единица измерения')
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.title} / {self.measure}'

    class Meta:
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    """Рецепты"""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    tags = MultiSelectField(choices=TAG_CHOICES, blank=True,
                            null=True, verbose_name='Теги')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления')
    image = models.ImageField(
        upload_to='recipes/',
        blank=True, null=True,
        verbose_name='Изображение')
    ingredient = models.(Ingredient,
                                  on_delete=models.SET_NULL,
                                  related_name='',
                                  verbose_name='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'



