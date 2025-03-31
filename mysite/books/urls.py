from django.urls import path
from . import views
from .views import (BookCreateView, GenreListView, GenreDetailView, AuthorCreateView, UserLogoutView)

app_name = 'books'
urlpatterns = [
    path('', views.GenreListView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genre/<int:pk>/add-book/', views.BookCreateView.as_view(), name='book_create'),
    path('author/new/', views.AuthorCreateView.as_view(), name='author_create'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),

]