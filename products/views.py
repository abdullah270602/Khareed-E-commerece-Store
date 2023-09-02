from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,WishlistItem,Wishlist
from cart.models import Cart,CartItem
from django.db.models import Q
from .models import Product

def search(request):
    query = request.GET.get('query','')
    products = []
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(category__category_name__icontains=query)
        )
    
    stars = [1,2,3,4,5]
    context = {'products': products, 'query': query,'stars':stars}
    return render(request, 'products/browse.html', context)



def check_item_in_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    users_cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.filter(cart=users_cart, product=product)
    
    return cart_item.exists() 


def check_item_in_wishlist(request,pk):
    product = get_object_or_404(Product,pk=pk)
    user_wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item = WishlistItem.objects.filter(wishlist=user_wishlist, product=product)
    
    return wishlist_item.exists() 


def product_detail(request,uuid):
    product = get_object_or_404(Product, id=uuid)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    
    item_in_wishlist = False
    item_in_cart = False
    if request.user.is_authenticated:
        # Checking if the product is laredy in wishlist
        item_in_wishlist = check_item_in_wishlist(request,uuid)
        
        # Checking if the product is alaredy in cart
        item_in_cart = check_item_in_cart(request, uuid)
        
    context = {'product':product, 'related_products':related_products, 'item_in_cart':item_in_cart,'item_in_wishlist':item_in_wishlist}
    return render(request,'products/product_detail.html',context)


def wishlist(request):
    user_wishlist , _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = WishlistItem.objects.filter(wishlist = user_wishlist)
    
    
    
    context = {'wishlist_items':wishlist_items,}
    return render(request,'products/wishlist.html',context)


def add_to_wishlist(request,pk):
    item = Product.objects.get(pk=pk)
    
    user_wishlist , _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items, wishlist_items_created = WishlistItem.objects.get_or_create(wishlist = user_wishlist,product = item) 
    
    
    # if its already in the list
    if not wishlist_items_created:
        return redirect ('products:product_detail',pk)
    else:
        wishlist_items.save()
        
    return redirect ('products:product_detail',pk)
    
    
def remove_from_wishlist(request,pk):
    if request.method == 'POST':
        wishlist_item = get_object_or_404(WishlistItem,pk=pk)
        wishlist_item.delete()
        
        
    return redirect('products:wishlist')