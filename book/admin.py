from django.contrib import admin
from .models import Author, Book, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'created_at',)
    list_display_links = ('id', 'first_name', 'last_name', 'birth_date', 'created_at',)
    search_fields = ('id', 'first_name', 'birth_date',)
    ordering = ('created_at',)


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'author', 'price', 'count', 'created_at',)
    list_display_links = ('id', 'title', 'slug', 'description', 'author', 'price', 'count', 'created_at',)
    prepopulated_fields = {'slug': ('title',)}
