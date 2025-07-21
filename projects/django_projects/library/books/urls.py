from .views import AuthorViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name = 'books'
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]