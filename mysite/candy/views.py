from django.shortcuts import render, redirect, get_object_or_404
from .models import Candy, CandyDescription
from .forms import CandyForm, CandyDesForm

# List all candies
def candy_list(request):
    candies = Candy.objects.all()
    return render(request, 'candy_list.html', {'candies': candies})

# Create a new candy
def candy_create(request):
    if request.method == "POST":
        form = CandyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candy_list')
    else:
        form = CandyForm()
    return render(request, 'candy_form.html', {'form': form})

# Delete a candy
def candy_delete(request, pk):
    candy = get_object_or_404(Candy, pk=pk)
    if request.method == "POST":
        candy.delete()
        return redirect('candy_list')
    return render(request, 'candy_confirm_delete.html', {'candy': candy})

# List candy descriptions
def description_list(request):
    descriptions = CandyDescription.objects.all()
    return render(request, 'description_list.html', {'descriptions': descriptions})

# Create a new candy description
def description_create(request):
    if request.method == "POST":
        form = CandyDesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('description_list')
    else:
        form = CandyDesForm()
    return render(request, 'description_form.html', {'form': form})

# Create your views here.
