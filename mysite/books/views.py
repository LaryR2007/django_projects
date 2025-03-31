from django import forms
from django.shortcuts import render
from django.views import generic, View
from .models import Book, Genre, Author
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404

# Create your views here.
class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'books/genre_list.html'
    context_object_name = 'genres'

class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = 'books/genre_detail.html'
    context_object_name = 'genre'

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres']

    author = forms.ModelChoiceField(queryset=Author.objects.all())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'books/book_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Assign the current user as the owner of the book
        return super().form_valid(form)

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('books:author_list')  # Redirect to the list of authors after successful creation

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Set the owner to the current logged-in user
        return super().form_valid(form)
    
class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'

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