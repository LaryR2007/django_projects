from django.shortcuts import render, redirect, get_object_or_404
from .models import Candy, CandyDescription
from .forms import CandyForm, CandyDescriptionForm

# List all candies
def candy_list(request):
        candies = Candy.objects.all()
        return render(request, 'candy/candy_list.html', {'candies': candies})

# Create a new candy
def candy_create(request):
    if request.method == "POST":
        form = CandyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candy_list')
    else:
        form = CandyForm()
    return render(request, 'candy/candy_form.html', {'form': form})

# Delete a candy
def candy_delete(request, pk):
    candy = get_object_or_404(Candy, pk=pk)
    if request.method == "POST":
        candy.delete()
        return redirect('candy_list')
    return render(request, 'candy/candy_confirm_delete.html', {'candy': candy})

# List candy descriptions
def description_detail(request):
    model = CandyDescription
    template_name = 'Candy/description_list.html' 
    
# Create a new candy description
def description_create(request):
    if request.method == "POST":
        form = CandyDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('description_list')
    else:
        form = CandyDescriptionForm()
    return render(request, 'candy/description_form.html', {'form': form})

# Create your views here.
