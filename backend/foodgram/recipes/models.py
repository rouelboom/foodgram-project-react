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
    measure = models.CharField(max_length=100,
                               verbose_name='Единица измерения')
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.title} / {self.measure}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    """Рецепты"""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    tags = MultiSelectField(choices=TAG_CHOICES, blank=True,
                            null=True, verbose_name='Теги')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(verbose_name=
                                               'Время приготовления')
    ingredients = models.ManyToManyField(
        Ingredient, through="IngredientAmount"
    )
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Tag(models.Model):
    """Тeг"""
    title = models.CharField(max_length=150,
                             verbose_name='Название')
    color = models.CharField(max_length=25,
                             verbose_name='Цвет(hex)')
    slug = models.fields.SlugField(unique=True, max_length=200,
                                   verbose_name="Уникальный адрес")

    class Meta:
        verbose_name = 'Тeг'
        verbose_name_plural = 'Тeги'


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="favorite_user",
                             verbose_name="Пользователь"
                             )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="favorite_recipe")

    class Meta:
        verbose_name_plural = "Список избранного"
        verbose_name = "Список в избранного"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite_recipe',
            ),
        ]


class ShoppingCart(models.Model):
    recipes_shop = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                                     related_name="shop_recipe"
                                     )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Пользователь"
                             )

    class Meta:
        verbose_name_plural = "Список покупок"
        verbose_name = "Список в покупок"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipes_shop'],
                name='unique_shop_cart',
            ),
        ]


class IngredientAmount(models.Model):
    ingredients = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="ingredient_amount"
    )
    recipes = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredient_amount")
    amount = models.IntegerField(verbose_name="Кол-во")

    class Meta:
        verbose_name_plural = "Кол-во ингридиентов"
        verbose_name = "Кол-во ингридиента"
        constraints = [
            models.UniqueConstraint(
                fields=['recipes', 'ingredients'],
                name='unique_ingredients',
            ),
        ]