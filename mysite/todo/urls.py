from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', views.ItemList.as_view()),
    path('<pk>/', views.ItemDetail.as_view()),
]
