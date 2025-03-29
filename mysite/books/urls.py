from django.urls import path
from . import views
from .views import (BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, UserLogoutView)

app_name = 'books'
urlpatterns = [
    path('', views.GenreListView.as_view(), name='genre_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('author/new/', views.AuthorCreateView.as_view(), name='author-create'),
    path('genre/new/', views.GenreCreateView.as_view(), name='genre-create'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
]

