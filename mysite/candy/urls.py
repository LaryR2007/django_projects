from django.urls import path
from . import views

urlpatterns = [
    path('', views.candy_list, name='candy_list'),
    path('candy/new/', views.candy_create, name='candy_create'),
    path('candy/<int:pk>/delete/', views.candy_delete, name='candy_delete'),
    path('descriptions/', views.description_list, name='description_list'),
    path('description/new/', views.description_create, name='description_create'),
]