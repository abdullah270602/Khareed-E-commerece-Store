from django.db import models
from django.core.validators import MinValueValidator,FileExtensionValidator
import uuid
from decimal import Decimal
from django.utils.text import slugify
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable= False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique= True,null=True, blank=True)
    category_image = models.ImageField(upload_to="categories" ,
                                       validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    
    def __str__(self) -> str:
         return self.category_name
    
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique= True,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.99'))])
    product_description = models.TextField()
    
    def __str__(self) -> str:
        return self.product_name
    
    # Overiding the save method
    def save(self, *args,**kwargs):
        if self.slug is None:
            self.slug = slugify(f"{self.category.category_name} { self.product_name}")
        super().save(*args,**kwargs)
    

class ProductImage(models.Model):
        product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="product_images")
        product_image = models.ImageField(upload_to="products",
                                          validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
        
        def __str__(self) -> str:
            return (f"{self.product} Image")
        
        
class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wishlist')
    
    
    
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='wishlist_items')
    
    
    class Meta:
        unique_together = ['wishlist', 'product']