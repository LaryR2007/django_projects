from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.candy_list, name='candy_list'),
    path('candy/new/', views.candy_create, name='candy_create'),
    path('candy/<int:pk>/delete/', views.candy_delete, name='candy_delete'),
    path('candy/<int:candy_id>/', views.candy_detail, name='candy_detail'),
    path('colors/<str:color_name>/', views.candies_by_color, name='candies_by_color'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]