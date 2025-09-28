from django.contrib import admin
from .models import Book  # import your model

# Register your models here.

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    list_filter = ('author', 'publication_year')           # sidebar filters
    search_fields = ('title', 'author')                    # search box
