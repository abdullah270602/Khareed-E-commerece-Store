from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart,CartItem
from decimal import Decimal
from django.urls import reverse


@login_required
def add_to_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    
    users_cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=users_cart, product=product)
    
    # If the cart_item is already in the cart, increment the QTY
    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    
    request.session['cart_total_items'] = users_cart.get_total_items()

    
    referring_url = request.META.get('HTTP_REFERER', reverse('accounts:home'))
    
    return redirect(referring_url)


@login_required
def cart(request):
    #Retriving the users cart
    users_cart, _ = Cart.objects.get_or_create(user=request.user)
    subtotal = round(users_cart.get_total_cost(),2)
    shipping = Decimal('0.00')
    total_cost = round(subtotal + shipping,2)
    
    cart_items = users_cart.cart_item.all()
    
    
    context = {'cart_items':cart_items,'users_cart' : users_cart, 'subtotal':subtotal, 'shipping':shipping,'total_cost':total_cost}
    return render(request,'cart/cart.html',context)


@login_required
def remove_cart_item(request, pk):
    users_cart, _ = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
            cart_item = get_object_or_404(CartItem, pk=pk)
            cart_item.delete()
            request.session['cart_total_items'] = users_cart.get_total_items()
            
    return redirect('cart:cart')       