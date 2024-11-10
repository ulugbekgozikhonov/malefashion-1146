from django import template

from products.models import Product, WishList

register = template.Library()


@register.simple_tag
def get_cart_info(request):
	product_ids = request.session.get("cart", [])
	count = len(product_ids)
	total = 0

	products = Product.objects.filter(id__in=product_ids).all()

	for product in products:
		total += product.real_price

	return count, round(total / 12800, 1)


@register.simple_tag
def in_cart(request, pk):
	product_ids = request.session.get("cart", [])
	print("id", pk, product_ids)
	return str(pk) in product_ids


# if pk in product_ids:
# 	return True
# else:
# 	return False

@register.simple_tag
def in_wishlist(request, product):
	return WishList.objects.filter(user=request.user, product=product).exists()
