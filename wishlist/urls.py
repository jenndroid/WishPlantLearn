"""Defines url patterns for wishlist"""

from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    # Wishlist 'homepage' - i.e just wishlist
    path('wishlist/', views.wishlist, name='wishlist')
]