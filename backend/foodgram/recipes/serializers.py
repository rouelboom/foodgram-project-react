from django.shortcuts import get_object_or_404
from rest_framework import serializers

from users.serializers import CustomUserSerializer
from .common_handlers import Base64ImageField
# from .fields import Base64ImageField
from .models import (FavoriteRecipe, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag, User)

from .models import Recipe, Ingredient, Tag, User


class RecipeViewSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True,)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Recipe
        # depth = 2


class IngredientViewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient


class IngredientAmountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = IngredientAmount


class TagViewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag
        # depth = 1

    # def validate(self, data):
    #     if self.context['request'].method == 'POST':
    #         title_id = self.context['view'].kwargs['title_id']
    #         current_title = get_object_or_404(Title, id=title_id)
    #         if current_title.reviews.filter(
    #                 author=self.context['request'].user):
    #             raise serializers.ValidationError("One user - "
    #                                               "one review for the title")
    #     return data

#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ('id',)
#         model = Category
#         lookup_field = 'slug'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailConfirmCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=50)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        ]

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.content = validated_data.get('content', instance.content)
            instance.created = validated_data.get('created', instance.created)
            return instance
