# Django Admin Configuration for Book Model

1. Open `bookshelf/admin.py` and import the Book model.
2. Register the Book model with admin:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
