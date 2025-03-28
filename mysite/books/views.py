from django.shortcuts import render
from django.views import generic, View
from .models import Book
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
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