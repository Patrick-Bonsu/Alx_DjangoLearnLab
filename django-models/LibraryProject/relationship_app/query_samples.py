import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    # ✅ Using objects.filter instead of reverse relation
    return Book.objects.filter(author=author)

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage
if __name__ == "__main__":
    print("Books by Author John Doe:", books_by_author("John Doe"))
    print("Books in City Library:", books_in_library("City Library"))
    print("Librarian of City Library:", librarian_of_library("City Library"))
