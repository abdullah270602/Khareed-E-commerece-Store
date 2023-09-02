from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('add-to-cart/<str:pk>',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_cart_item/<int:pk>/', views.remove_cart_item, name='remove_cart_item'),
]