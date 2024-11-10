from django.urls import path
from .views import add_or_remove_to_cart, add_to_wishlist

app_name = 'products'

urlpatterns = [
	path('add-to-cart/<str:pk>/', add_or_remove_to_cart, name='add-to-cart'),
	path('add-to-wishlist/<str:pk>/', add_to_wishlist, name='add-to-wishlist')
]
