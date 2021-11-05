import uuid

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django_filters import rest_framework as dfilters
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (RecipeViewSerializer, TagViewSerializer,
                          UserSerializer, IngredientViewSerializer,
                          EmailConfirmCodeSerializer)
from .models import Recipe, Tag, Ingredient


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        queryset = Recipe.objects.all()
        # print(queryset)
        return queryset

    def perform_create(self, serializer):
        # review = get_object_or_404(Recipe, id=self.kwargs['review_id'])
        # serializer.save(review=review, author=self.request.user)
        serializer.save()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        # if self.request.data
        queryset = Tag.objects.all()
        return queryset

    def perform_create(self, serializer):
        # review = get_object_or_404(Recipe, id=self.kwargs['review_id'])
        # serializer.save(review=review, author=self.request.user)
        serializer.save()


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        return queryset


# class BaseViewSet(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
# ):
#     pass
#
#
# class CategoryViewSet(BaseViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminOrReadOnly]
#     lookup_field = 'slug'
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', ]
#     http_method_names = ['get', 'post', 'delete']
#
#
# class GenreViewSet(BaseViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     permission_classes = [IsAdminOrReadOnly]
#     lookup_field = 'slug'
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', ]
#     http_method_names = ['get', 'post', 'delete']