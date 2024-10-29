from django.shortcuts import render
from django.views.generic import ListView

from .models import Banner
from products.models import Product,Category , Brand , Color,Tags


def home_view(request):
	banners = Banner.objects.filter(status=True)
	context = {
		"banners": banners
	}

	return render(request, "index.html", context)


class HomePageView(ListView):
	template_name = "index.html"
	context_object_name = "banners"
	model = Banner

	def get_queryset(self):
		return self.model.objects.filter(status=True)


def shop_view(request):
	products = Product.objects.order_by("-created_at")
	categories = Category.objects.order_by("-created_at")
	brands = Brand.objects.order_by("-created_at")
	colors = Color.objects.all()
	tags = Tags.objects.all()

	context = {
		"products": products,
		"categories": categories,
		"brands": brands,
		"colors": colors,
		"tags": tags


	}
	return render(request, "shop.html", context)
