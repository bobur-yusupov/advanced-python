from .views import AuthorViewSet, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("author", AuthorViewSet, basename="author")
router.register("book", BookViewSet, basename="book")

urlpatterns = [
    path('library/', include(router.urls)),
]