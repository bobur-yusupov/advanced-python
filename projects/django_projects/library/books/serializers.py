from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )
    class Meta:
        model = Author
        fields = ["id", "name", "bio", "url", "books"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_date", "isbn", "url"]
