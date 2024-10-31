from django.shortcuts import render, redirect


def add_to_cart(request, pk):
	current_path = request.META["HTTP_REFERER"]

	cart = request.session.get("cart", [])

	if pk in cart:
		cart.remove(pk)
	else:
		cart.append(pk)

	request.session["cart"] = cart

	print(cart)

	return redirect(current_path)
