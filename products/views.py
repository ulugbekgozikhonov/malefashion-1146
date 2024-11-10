from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from products.models import Product, WishList


def add_or_remove_to_cart(request, pk):
	current_path = request.META["HTTP_REFERER"]

	cart = request.session.get("cart", [])

	if pk in cart:
		cart.remove(pk)
	else:
		cart.append(pk)

	request.session["cart"] = cart

	print(cart)

	return redirect(current_path)


@login_required
def add_to_wishlist(request, pk):
	user = request.user
	product = Product.objects.filter(id=pk).first()

	try:
		WishList.objects.create(user=user, product=product)
	except:
		WishList.objects.filter(user=user, product=pk).delete()

	return redirect(request.META["HTTP_REFERER"])
