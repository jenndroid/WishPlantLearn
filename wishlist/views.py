from django.shortcuts import render

from .models import Plant

# Create your views here.
def wishlist(request):
    """Show all plants"""
    plants = Plant.objects.all()
    context = {'plants' : plants}
    return render(request, 'wishlist/wishlist.html', context)