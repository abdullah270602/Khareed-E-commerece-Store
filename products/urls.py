from django.urls import path
from . import views


app_name='products'


urlpatterns = [
    path('product/<uuid:uuid>/',views.product_detail,name='product_detail'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('add-to-wishlist/<str:pk>',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove-from-wishlist/<str:pk>',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('remove-from-wishlist/<str:pk>',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('Search/',views.search,name='search'),
]