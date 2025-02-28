from django.urls import path
from django.views.generic import TemplateView 
from . import views

app_name = 'todo'

urlpatterns = [
    path('items', views.TodoListView.as_view(), name='items'),
    path('item/<int:pk_from_url>', views.TodoDetailView.as_view(), name='item'),
    path('add/', views.AddItemView.as_view(), name='add_item'),
    path(
        '<int:pk>/delete/',
        views.DeleteItemView.as_view(),
        name='delete_item'
    ),
]