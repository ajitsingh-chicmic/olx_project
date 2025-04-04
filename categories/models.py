from datetime import datetime
from django.db import models
from account.models import User
from .choices import ProductStatus,AvailabilityStatus
import algoliasearch_django as algoliasearch, pytz

# Create your models here.
class Category(models.Model):
    
    category_type=models.CharField(max_length=100)
    def __str__(self):
        return self.category_type
class Subcategory(models.Model):
    U_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=100)
    def __str__(self):
        return self.subcategory_name



from django.db import models
    


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="product_cat")
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # Keep as IntegerField if storing prices as whole numbers
    description = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=ProductStatus.STATUS_CHOICES,
        default=ProductStatus.STATUS_CHOICES[0][0]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=100, null=True)
    availability = models.CharField(
        max_length=10,
        choices=AvailabilityStatus.AVAILABILITY_CHOICES,
        default=AvailabilityStatus.AVAILABILITY_CHOICES[0][0]
    )
    display_photo=models.ImageField(default=None)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    @property
    def location(self):
        """Return formatted location string"""
        if self.district:
            return f"{self.district}, {self.city}, {self.state}"
        return f"{self.city}, {self.state}"

class Images(models.Model):
    P=models.ForeignKey(Products,on_delete=models.CASCADE)
    image = models.ImageField(default=None)
    # def __str__(self):
    #     return self.P
# class car:
#     if isinstance(car,Products):
#         schema=products.objects.get('car')

class car(Products):
    km_driven=models.CharField(max_length=10)
    mileage=models.CharField(max_length=11)
    variant=models.CharField(max_length=12)
class Bike(Products):
        km_driven=models.CharField(max_length=10)
        Brand=models.CharField(max_length=200)
        Year=models.DateField()
class Furniture(Products):
    Furniture_type=models.CharField(max_length=200)
    wood_name=models.CharField(max_length=100)
class Electronics(Products):
    Electrnics_type=models.CharField(max_length=200)
    Warranty_left=models.CharField(max_length=200,default='Out Of warranty')
    Brand_name=models.CharField(max_length=200)
class Bicycle(Products):
    Brand_name=models.CharField(max_length=200)
    Bicycle_category=models.CharField(max_length=100)


class SubCategoryDetails(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class ProductSubcategoryDetails(models.Model):
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    subcategorydetails=models.ForeignKey(SubCategoryDetails,on_delete=models.CASCADE)
    value=models.CharField(max_length=100)
class UserFavourites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    



    
    











