from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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


# --- User Registration View ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('list_books')  # redirect to some page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- User Login View ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('list_books')  # redirect to some page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# --- User Logout View ---
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Logged out successfully.")
        return redirect('login')
    return render(request, 'relationship_app/logout.html')