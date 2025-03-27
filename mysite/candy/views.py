
from django.shortcuts import render, redirect, get_object_or_404
from .models import Candy, CandyDescription, Color
from .forms import CandyForm, CandyDescriptionForm, Color
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


# List all candies
def candy_list(request):
        candies = Candy.objects.all()
        return render(request, 'candy/candy_list.html', {'candies': candies})

def candy_detail(LoginRequiredMixin, DetailView):
    candy = get_object_or_404(Candy, id=candy_id)
    login_url = '/login/' 
    return render(request, 'candy/candy_detail.html', {'candy': candy})

# Create a new candy
def candy_create(request):
    success_url = reverse('candy_list')
    login_url = '/login/'
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

def candy_detail(request, candy_id):
    candy = get_object_or_404(Candy, id=candy_id)
    descriptions = candy.descriptions.all()
    success_url = reverse('candy_list')
    login_url = '/login/'

    # Show form only if no description exists
    form = None
    if not descriptions and request.method != "POST":
        form = CandyDescriptionForm()

    if request.method == "POST":
        form = CandyDescriptionForm(request.POST)
        if form.is_valid():
            description = form.save(commit=False)
            description.candy = candy
            description.save()
            form.save_m2m()  # Save many-to-many relationship
            return redirect('candy_detail', candy_id=candy.id)  # Refresh page without form

    return render(request, 'candy/candy_detail.html', {
        'candy': candy,
        'descriptions': descriptions,
        'form': form
    })

# View to edit colors and assign candies
def color_update(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == "POST":
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            return redirect('color_list')  # Redirect back to colors page
    else:
        form = ColorForm(instance=color)

    return render(request, 'candy/color_form.html', {'form': form, 'color': color})

def candies_by_color(request, color_name):
    color = get_object_or_404(Color, name=color_name)  # Get color by name
    candies = Candy.objects.filter(descriptions__colors=color).distinct()  # Get candies with that color
    
    return render(request, 'candy/candies_by_color.html', {'color': color, 'candies': candies})



# Create your views here.
