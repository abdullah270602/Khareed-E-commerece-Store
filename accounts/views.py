from django.shortcuts import render

from django.shortcuts import render , redirect
from .forms import SignUpForm
from products.models import Product
from cart.models import Cart

def SignUp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('accounts:home')
    else:
        form = SignUpForm()
        
    context = {'form' : form , 'title' : 'SignUp'}
    
    return render (request,'accounts/signup.html',context)


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')
    
    total_items = 0
    if request.user.is_authenticated:
        # TO calculate the total number of items in the users cart
        users_cart, _ = Cart.objects.get_or_create(user=request.user)
        total_items = users_cart.get_total_items()
        
    request.session['cart_total_items'] = total_items
    
    
    stars = [1,2,3,4,5]
    context = {'latest_products':latest_products, 'stars' : stars,}
    return render(request,'accounts/home.html',context)

def terms(request):
    context = {}
    return render(request,'accounts/terms&conditions.html',context)


