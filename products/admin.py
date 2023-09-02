from django.contrib import admin
from .models import Category,Product,ProductImage,WishlistItem,Wishlist
from django.utils.html import format_html




class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src="{object.category_image.url}" width="40" style="border-radius: 30px;"  />')
    
    
    thumbnail.short_description = 'Image'
    
    list_display = ('id','thumbnail','category_name')
    list_display_links = ('id','thumbnail','category_name')
    list_filter = ('category_name',)
    search_fields = ('id','category_name',)
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','category','price')
    list_display_links = ('id','product_name','category','price')
    list_filter = ('product_name','category',)
    search_fields = ('id','product_name','category','price')
    
    
    
class ProductImageAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src="{object.product_image.url}" width="40" style="border-radius: 30px;"  />')
    
    
    thumbnail.short_description = 'Image'
    
    list_display = ('id','thumbnail','product')
    list_display_links = ('id','thumbnail','product')
    search_fields = ('id','product',)
    
    
    
    
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(WishlistItem)
admin.site.register(Wishlist)