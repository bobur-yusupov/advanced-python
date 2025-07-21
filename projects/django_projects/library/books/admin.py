from django.contrib import admin

from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_date', 'isbn')
    search_fields = ('title', 'author__name', 'genre__name', 'isbn')
    list_filter = ('author', 'genre', 'published_date')
    ordering = ('title',)