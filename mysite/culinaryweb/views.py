from django.shortcuts import render
from django.views import generic
from .models import Service, Detail

class ServiceIndexView(generic.ListView):
    model = Service
    template_name = 'culinaryweb/service_list.html'
    context_object_name = 'services'

class DetailView(generic.DetailView):
    model = Detail
    template_name = 'culinaryweb/service_detail.html'
# Create your views here.
