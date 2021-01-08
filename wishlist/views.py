from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Plant
from .forms import PlantForm

# Create your views here.
@login_required
def wishlist(request):
    """Show all plants on wishlist"""
    plants = Plant.objects.filter(owner=request.user)
    purchased_plants = plants.filter(purchased='True')
    wanted_plants = plants.filter(purchased='False')
    context = {'purchased_plants' : purchased_plants, 'wanted_plants' : wanted_plants}
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def new_plant(request):
    """Add new plant to wishlist"""
    if request.method != 'POST':
        # No data submitted- show only the blank form
        form = PlantForm()
    else: 
        # POST data submitted, process info
        form = PlantForm(request.POST)

        if form.is_valid(): 
            new_plant = form.save(commit=False)
            new_plant.owner = request.user
            new_plant.save()
            return HttpResponseRedirect(reverse('wishlist:wishlist'))

    context = {'form': form}
    return render(request, 'wishlist/new_plant.html', context)

@login_required
def edit_plant(request, plant_id):
    """Edit plant on the wishlist"""
    plant = Plant.objects.get(id=plant_id)

    if request.method != 'POST':
        form = PlantForm(instance=plant)
    else:
        form = PlantForm(instance=plant, data=request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('wishlist:wishlist'))
    
    context = {'plant': plant, 'form': form}
    return render(request, 'wishlist/edit_plant.html', context)




