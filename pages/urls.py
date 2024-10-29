from django.urls import path
from .views import HomePageView, ShopView, shop_detail_view

app_name = "pages"

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path("shop/", ShopView.as_view(), name="shop"),
	path("shop-detail/<str:pk>/", shop_detail_view, name="shop-detail"),
]
