from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView



app_name = 'viewsbasics'
urlpatterns = [
    path('', TemplateView.as_view(template_name='viewsbasics/index.html')),
    path('funktionally', views.funktionally),
    path('danger', views.danger),
    path('safer', views.safer),
    path('prettyurldata/<thing>', views.prettyurldata),
    path('bounce', views.bounce),
    path('name/<name>/', views.Name.as_view()),
    path('num/<num>/', views.Num.as_view()),
    path('word/<word>/', views.Word.as_view()),
    path('bmi/<weight>/<height>/', views.BMI.as_view()),
    path('calc/<length>/<height>/', views.Calc.as_view()),
]    
