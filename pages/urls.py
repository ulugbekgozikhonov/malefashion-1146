from django.urls import path
from .views import HomePageView, shop_view

app_name = "pages"

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path("shop/", shop_view, name="shop")
]
