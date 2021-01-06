"""Defines url patterns for wishlist"""

from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    # Display wishlist- i.e, all plants
    path('wishlist/', views.wishlist, name='wishlist'), 

    # Add a new plant to the wishlist
    path('new_plant', views.new_plant, name='new_plan')
]