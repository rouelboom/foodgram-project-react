from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from colorfield.fields import ColorField


User = get_user_model()

# Возможные варианты выбора для поля tags
TAG_CHOICES = (('breakfast', 'Завтрак'),
               ('lunch', 'Обед'),
               ('dinner', 'Ужин'))


class Ingredient(models.Model):
    """Ингредиенты"""
    name = models.CharField(max_length=150,
                            verbose_name='Название ингредиента')
    measurement_unit = models.CharField(max_length=100,
                                        verbose_name='Единица измерения')
    # amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    """Рецепты"""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='Автор')
    name = models.CharField(max_length=100,
                            verbose_name='Название рецепта')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    # tags = MultiSelectField(choices=TAG_CHOICES, blank=True,
    #                         null=True, verbose_name='Теги')
    tags = models.ManyToManyField("Tag")
    text = models.TextField(blank=True, null=True,
                            verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(verbose_name=
                                               'Время приготовления')
    ingredients = models.ManyToManyField(
        Ingredient, through="IngredientAmount"
    )
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Tag(models.Model):
    """Тeг"""
    name = models.CharField(max_length=150,
                             verbose_name='Название')
    color = ColorField(default='#FF0000',
                             verbose_name='Цвет(hex)')
    slug = models.fields.SlugField(unique=True, max_length=200,
                                   verbose_name="Уникальный адрес")

    class Meta:
        verbose_name = 'Тeг'
        verbose_name_plural = 'Тeги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


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