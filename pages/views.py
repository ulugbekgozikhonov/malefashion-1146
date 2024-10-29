from django.shortcuts import render
from django.views.generic import ListView

from .models import Banner
from products.models import Product, Category, Brand, Color, Tags, Size


# def home_view(request):
# 	banners = Banner.objects.filter(status=True)
# 	context = {
# 		"banners": banners
# 	}
#
# 	return render(request, "index.html", context)


class HomePageView(ListView):
	template_name = "index.html"
	context_object_name = "banners"
	model = Banner

	def get_queryset(self):
		return self.model.objects.filter(status=True)


# def shop_view(request):
# 	products = Product.objects.order_by("-created_at")
# 	categories = Category.objects.order_by("-created_at")
# 	brands = Brand.objects.order_by("-created_at")
# 	colors = Color.objects.all()
# 	tags = Tags.objects.all()
#
# 	context = {
# 		"products": products,
# 		"categories": categories,
# 		"brands": brands,
# 		"colors": colors,
# 		"tags": tags
#
#
# 	}
# 	return render(request, "shop.html", context)


class ShopView(ListView):
	template_name = "shop.html"
	model = Product
	context_object_name = "products"

	def get_queryset(self):
		return Product.objects.order_by("-created_at")

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context["colors"] = Color.objects.all()
		context["categories"] = Category.objects.order_by("-created_at")
		context["brands"] = Brand.objects.order_by("-created_at")
		context["sizes"] = Size.objects.all()
		context["tags"] = Tags.objects.all()

		return context


def shop_detail_view(request, pk):
	product = Product.objects.filter(id=pk).first()
	context = {
		"product": product
	}
	return render(request=request, template_name="shop-details.html", context=context)
