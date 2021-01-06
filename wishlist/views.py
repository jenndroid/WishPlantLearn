from django.shortcuts import render

# Create your views here.
def wishlist(request):
    """The wishlist display page"""
    return render(request, 'wishlist/wishlist.html')