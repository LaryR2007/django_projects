from django.shortcuts import render
from django.views import generic
from .models import Item, Detail

class ListView(generic.ListView):
    model = Item
    template_name = 'todo/item_list.html'
    context_object_name = 'items'

class DetailView(generic.DetailView):
    model = Detail
    template_name = 'todo/item_detail.html'

# Create your views here.
