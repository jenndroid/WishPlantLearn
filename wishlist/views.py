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
    plants = Plant.objects.all()
    context = {'plants' : plants}
    return render(request, 'wishlist/wishlist.html', context)


def new_plant(request):
    """Add new plant to wishlist"""
    if request.method != 'POST':
        # No data submitted- show only the blank form
        form = PlantForm()
    else: 
        # POST data submitted, process info
        form = PlantForm(request.POST)

        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('wishlist:wishlist'))

    context = {'form': form}
    return render(request, 'wishlist/new_plant.html', context)
