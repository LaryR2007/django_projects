from django.urls import path
from . import views

app_name = "culinaryweb"
urlpatterns = [
    path('', views.ServiceIndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
]

