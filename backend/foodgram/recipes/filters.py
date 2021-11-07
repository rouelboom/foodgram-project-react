from django_filters import rest_framework as filters

from .models import Recipe


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug')
    is_favorited = filters.BooleanFilter(
        method='get_favorite',
    )
    is_in_shopping_cart = filters.filters.BooleanFilter(
        method='get_shop_cart',
    )

    def get_favorite(self, queryset, name, value):
        if self.request.query_params.get('is_favorited'):
            return queryset.filter(
                favorite_recipe__user=self.request.user
            )
        return queryset

    def get_shop_cart(self, queryset, name, value):
        if self.request.query_params.get('is_in_shopping_cart'):
            return queryset.filter(
                shop_recipe__user=self.request.user
            )
        return queryset

    class Meta:
        model = Recipe
        fields = ['author', 'tags', 'is_favorited', 'is_in_shopping_cart']
