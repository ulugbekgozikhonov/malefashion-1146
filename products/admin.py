from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "price"]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
	list_display = ["id", "product"]
