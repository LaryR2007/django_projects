from django.views import View
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

from todo.models import ToDo 

# Create your views here.

class TodoListView(View):
    def get(self, request) :
        items = ToDo.objects.all()
        context = { 'todo_list': items }
        return render(request, 'todo/todos.html', context)


class TodoDetailView(View):
    def get(self, request, pk_from_url) :
        obj = ToDo.objects.get(pk=pk_from_url)
        context = { 'todo_item': obj }
        return render(request, 'todo/todo.html', context)


class AddItemView(generic.edit.CreateView):
    model = ToDo
    fields = '__all__'


class DeleteItemView(generic.edit.DeleteView):
    model = ToDo
    success_url = reverse_lazy('todo:items')


# Create your views here.
