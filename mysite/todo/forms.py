from django.forms import ModelForm
from todo.models import ToDo

class TodoForm(ModelForm):
    class Meta:
        mode = ToDo
        fields = '__all__'
