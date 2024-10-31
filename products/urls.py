from django.urls import path
from .views import add_to_cart

app_name = 'products'

urlpatterns = [
	path('add-to-cart/<str:pk>', add_to_cart, name='add-to-cart')
]
