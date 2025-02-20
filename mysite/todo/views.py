from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class ItemList(View):
    model = Item
    template_name = 'todo/item_list.html'
    context_object_name = 'items'

class ItemDetail(View):
    model = Item
    template_name = 'todo/item_detail.html'

# Create your views here.
