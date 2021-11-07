from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.CustomUserViewSet)

User = get_user_model()

urlpatterns = router.urls