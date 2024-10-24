from django.shortcuts import render
from django.views.generic import ListView

from .models import Banner


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
	return render(request, "shop.html")
