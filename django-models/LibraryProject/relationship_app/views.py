from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# --- Function-Based View: List all books ---
def list_books(request):
    books = Book.objects.all()
    # ✅ use app-specific template path
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View: Library details ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ app-specific path
    context_object_name = 'library'
