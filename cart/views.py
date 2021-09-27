from django.core.checks import messages
from products.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Cart , Order

# Create your views here.

#Add to Cart View

def add_to_cart(request , slug):
    item = get_object_or_404(Product , slug = slug)
    order_item , created = Cart.objects.get_or_create(
        item = item ,
        user = request.user
    )
    order_qs = Order.objects.filter(user=request.user , ordered=False) # isExists( request.user.id 's order )
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.Info(request, "This item quantity was updated.")
            return redirect("mainapp:home")
        else:
            order.orderitems.add(order_item)
            messages.Info(request, "This item was added to your cart.")
            return redirect("mainapp:home")
    else:
        order = Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.Info(request, "This item was added to your cart.")
        return redirect("mainapp:home")

def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug) # siExists( product of which slug is slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item) 
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.Info(request, "This item was removed from your cart.")
            return redirect("mainapp:home")
        else:
            messages.Info(request, "This item was not in your cart")
            return redirect("mainapp:home")
    else:
        messages.Info(request, "You do not have an active order")
        return redirect("core:home")


