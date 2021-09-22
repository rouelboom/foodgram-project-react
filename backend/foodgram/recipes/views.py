import uuid

from backend.foodgram.foodgram.settings import EMAIL_ADMIN
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

# from .filters import TitleFilter
# from .models import Category, Genre, Review, Title, User, UserConfirmationCode
# from .permissions import (IsAdminOrReadOnly, IsAuthorOrReadOnlyPermission,
#                           IsSuperuserPermission)
# from .serializers import (CategorySerializer, CommentViewSerializer,
#                           EmailConfirmCodeSerializer, EmailSerializer,
#                           GenreSerializer, ReviewViewSerializer,
#                           TitleCreateSerializer, TitleGetSerializer,
#                           UserSerializer)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission]

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer.save(review=review, author=self.request.user)


# class ReviewViewSet(viewsets.ModelViewSet):
#     serializer_class = ReviewViewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly,
#                           IsAuthorOrReadOnlyPermission]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['score', ]
#
#     def get_queryset(self):
#         title = get_object_or_404(Title, id=self.kwargs['title_id'])
#         queryset = title.reviews.all()
#         return queryset
#
#     def perform_create(self, serializer):
#         title = get_object_or_404(Title, id=self.kwargs['title_id'])
#         serializer.save(title=title, author=self.request.user)
#
#
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