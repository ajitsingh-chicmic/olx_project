from django.contrib import admin
from .models import Category,Subcategory,Products,Images,car,SubCategoryDetails,ProductSubcategoryDetails,UserFavourites

# Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['id','category_type']
    
@admin.register(Subcategory)
class subcategoryAdmin(admin.ModelAdmin):
    list_display=['id','U_id','subcategory_name']
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields]
    
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display=['P']
@admin.register(car)
class ImagesAdmin(admin.ModelAdmin):
   list_display = [field.name for field in car._meta.fields]
@admin.register(SubCategoryDetails)
class ImagesAdmin(admin.ModelAdmin):
   list_display = [field.name for field in SubCategoryDetails._meta.fields]
@admin.register(ProductSubcategoryDetails)
class ImagesAdmin(admin.ModelAdmin):
   list_display = [field.name for field in ProductSubcategoryDetails._meta.fields]
@admin.register(UserFavourites)
class ImagesAdmin(admin.ModelAdmin):
   list_display = [field.name for field in UserFavourites._meta.fields]


