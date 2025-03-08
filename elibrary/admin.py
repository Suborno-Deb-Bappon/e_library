from django.contrib import admin
from .models import Author, Genre, EBook, Borrowing, Rating

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'genre', 'licenses')
    list_filter = ('genre', 'publication_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('authors',)

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('user', 'ebook', 'borrow_date', 'return_date')
    list_filter = ('borrow_date',)
    search_fields = ('user__username', 'ebook__title')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'ebook', 'rating', 'comment', 'created_at')
    list_filter = ('ebook', 'rating')
    search_fields = ('user__username', 'ebook__title', 'comment')