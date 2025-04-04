from rest_framework import serializers
from .models import Category,Subcategory,Products,Images,car,Furniture,Bike,Bicycle
from account.models import User
from .models import UserFavourites
class categoriesSeerializer(serializers.Serializer):
    class Meta:
        model=Category
        fields='__all__'
    def validate(self, attrs):
        return attrs
class subcategorySerializer(serializers.Serializer):
    class Meta:
        model=Subcategory
        fields='__all__'
    def validate(self, attrs):
        return attrs
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['user','c','s','Product_name','price','description','status','state','city','district','detail']
class carserializer(serializers.ModelSerializer):
    class Meta:
        model=car
        fields=list(Productserializer.Meta.fields)+['km_driven','mileage','variant']
class Bikeserializer(serializers.ModelSerializer):
    class Meta:
        model=Bike
        fields=list(Productserializer.Meta.fields)+['km_driven','Brand','Year']
class furnitureserializer(serializers.ModelSerializer):
    class Meta:
        model=Bike
        fields=list(Productserializer.Meta.fields)+['furniture_type','wood_name',]
class Electronicsserializer(serializers.ModelSerializer):
    class Meta:
        model=Bike
        fields=list(Productserializer.Meta.fields)+['Electronics_type','warranty_left','Brand']
    
class Bicycleserializer(serializers.ModelSerializer):
    class Meta:
        model=Bike
        fields=list(Productserializer.Meta.fields)+['Brand_name','bicycle_category']
class displayProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields="__all__"


class displayAdSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Products
        fields="__all__"
        
    # def Validate(self, attrs):
    #     print(attrs)
    #     return super().validate(attrs)


class Logindisplayserializer(serializers.ModelSerializer):
    is_favourite=serializers.SerializerMethodField()
    class Meta:
        model=Products
        fields="__all__"
        extra_fields = ['is_favorite']
   
    def get_is_favourite(self,obj):
         
        
        
        return UserFavourites.objects.filter(
            user=User.objects.get(id=self.context['user']), 
            product=obj
         ).exists()

class UserFav(serializers.ModelSerializer):
    P=displayProductsSerializer(read_only=True)
   
    # def get_is_favourite(self,obj):
         
    #     return UserFavourites.objects.filter(
    #         user=User.objects.get(id=self.context['user']), 
    #         product=obj
    #      ).exists()
    
    class Meta:
        model=UserFavourites
        fields=['P']
    def to_representation(self, instance):
        product_data = self.fields['P'].to_representation(instance.product)
        product_data['is_favourite'] = True
        
        
        return product_data

class DisplayImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Images
        fields=["image"]
    
    


    


    