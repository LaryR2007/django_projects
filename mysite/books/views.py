from django.shortcuts import render
from django.views import generic, View
from .models import Book, Genre, Author
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'books/genre_list.html'

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genres']
    template_name = 'books/book_form.html'
    
    def get_initial(self):
        initial = super().get_initial()
        genre_id = self.request.GET.get('genre')
        if genre_id:
            initial['genres'] = [Genre.objects.get(id=genre_id)]
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'genres']
    template_name = 'books/book_form.html'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/' # Redirect after delete

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    template_name = 'books/author_form.html'

class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = ['name']
    template_name = 'books/genre_form.html'

class UserLogoutView(LogoutView):
    template_name = 'books/logout.html'

class DumpPython(View):
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('books:login') + "\n"
        resp += "Logout url: " + reverse('books:logout') + "\n\n"
        
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Authenticated: Yes\n"
        else:
            resp += "User is not logged in\n"
        
        resp += "</pre>\n"
        resp += "<a href=\"/\">Go back</a>"
        return HttpResponse(resp)