from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import Productserializer,carserializer,Bikeserializer,Bicycleserializer,furnitureserializer,Electronicsserializer,displayAdSerializer
from .models import Products,car,Furniture,Bike,Bicycle,Category,Subcategory,Images,SubCategoryDetails,ProductSubcategoryDetails,Products,UserFavourites
from rest_framework.response import Response
from django.db import transaction
from olx import settings
from account.models import User
from rest_framework import status
from django.db.models import F
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import Logindisplayserializer,UserFav,DisplayImageSerializer
from datetime import datetime
from django.db.models import Count
from django.db.models import Subquery, OuterRef
# Create your views here.
# class display products
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import transaction
from .serializers import carserializer, Bikeserializer, furnitureserializer, Bicycleserializer
from collections import namedtuple

class Sellproduct(APIView):
    http_method_names = ['post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        
        images=request.FILES
        

        
        try:
            with transaction.atomic():
                # category_id = data['c']
                category_id = int(data.get('c', 0))
                # user=request.post.get(id)
                # id=request.data.get(id)               
               
                
                user_id=request.user.id
               
                # print(user_id)
                data["user"]=user_id
                if category_id == 1:
                    serializer = carserializer(data=data)
                    


                elif category_id == 2:
                    serializer = Bikeserializer(data=data)
                elif category_id == 3:
                    serializer = furnitureserializer(data=data)
                elif category_id == 4:
                    serializer = Bicycleserializer(data=data)
                else:
                    return Response({'error': 'Invalid category ID'}, status=status.HTTP_400_BAD_REQUEST)

                # Validate the data first
                if serializer.is_valid():
                    Product_created= serializer.save()
                    for i in images.values():
                        img=Images.objects.create(P=Product_created,image=i)
                        img.save()
                        


                    return Response({'Msg': 'Data Saved'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DisplayAdViewCategory(generics.ListAPIView):
    http_method_names = ['get']
    
    
    # def list(self, request): http_method_names = ['get']
    def list(self, request):
        params=request.GET
        try:
            data=request.data
            page=int(params.get('page',1))
            limit=int(params.get('limit',2))
            offset=getoffset(page,limit)

            
            products=Products.objects.filter(Q(name__icontains=data["search"])|Q(category__category_type__icontains=data["search"])|
                                             Q(description__icontains=data["search"])|Q(subcategory__subcategory_name__icontains=data["search"])).filter(availability="Sold")[offset:limit+offset]
            # products1=Products.objects.filter(Category__category_type__icontains=data["search"]).filter(availability="Sold")[offset:limit+offset]
            # products2=Products.objects.filter(description__icontains=data["search"]).filter(availability="Sold")[offset:limit+offset]
            # products3=Products.objects.filter(Subcategory__subcategory_name__icontains=data["search"]).filter(availability="Sold")[offset:limit+offset]
            # print(products)
            product_list=displayAdSerializer(products,many=True)
            product_data=product_list.data
            return Response(data=product_data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error Occured":f"{e}"},status=status.HTTP_400_BAD_REQUEST)


class DisplayUsersAdView(generics.ListAPIView):
    http_method_names = ['get']
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def list(self, request):
        try:
            
            params = request.GET

            page = int(params.get('page', 1))
            limit = int(params.get('limit', 10))
            offset=getoffset(page,limit)

            # if page == 1:
            #     offset = 0
            # else:
            #     offset = (page - 1) * limit 


            id=request.user.id
            user=User.objects.get(id=id)
            products=Products.objects.filter(user=user)[offset:limit + offset]
    
            product_list=displayAdSerializer(products,many=True) 
            product_data=product_list.data
            # images=product_photos.objects.get(product=products.id)
            return Response(data=product_data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error Occured":f"{e}"},status=status.HTTP_400_BAD_REQUEST)

class FinDetails(APIView):
    http_method_names=['get']
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        product_id=data['id']
        try:
            product=Products.objects.get(id=product_id)
        except Exception as e:
            return Response({'msg':'This Product Doesnot exist'},status=status.HTTP_404_NOT_FOUND)
        result = (
        Products.objects
        .filter(id=product.id)  # Filter by product ID
        .annotate(
            title=F('productsubcategorydetails__subcategorydetails__title'),
            value=F('productsubcategorydetails__value')
        )
        .values('name', 'status', 'title', 'value')
    )
        dict1={}
        for item in result:
            title = item['title']
            value = item['value']
            dict1[title] = value
        dict1['description']=product.description
        dict1['price']=product.price
        dict1['status']=product.status
        dict1['Name']=product.name
        dict1['state']=product.state
        dict1['city']=product.city
        dict1['district']=product.district
        dict1['posted on ']=product.created_at

        return Response(dict1, status=status.HTTP_200_OK)   
        
         
class PutAd(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    http_method_names = ["post"]
    
    def post(self, request):
        try:
           
            data = request.data
            image_files=request.FILES.getlist("photos")
            
            category= Category.objects.select_related().get(category_type=data.get('category', 1))
         
            subcategory = Subcategory.objects.select_related().get(subcategory_name=data.get('subcategory', 1))
            print(category.id)
            print(subcategory.id)
            

            user=User.objects.get(id=data["user"])
            
            product_data = {
                "user": user,
                "category": category,
                "subcategory": subcategory,
                "name": data.get("title"),
                "price": data.get("price"),
                "description": data.get("description", ""),
                "state": data.get("state"),
                "city": data.get("city"),
                "district": data.get("district",""),
                "status": data.get("status", "old"),
                "display_photo":image_files[0]
            }
            from django.utils import timezone
            print(timezone.now())
            
            additional_fields = {k: v for k, v in data.items() if k not in [
               'user', 'category', 'subcategory', 'title', 'price', 'description',
                'state', 'city', 'district', 'status','photos','sellerName','mobileNumber'
            ]}
            print(timezone.now())
           
            with transaction.atomic():
                
                product_created = Products.objects.create(**product_data)
                print(additional_fields)
                print(timezone.now())
               
                for key, value in additional_fields.items():
                    print(key,value)
                    att = SubCategoryDetails.objects.filter(category=category).filter(subcategory=subcategory).get(title=key)
                    ProductSubcategoryDetails.objects.create(
                        Product=product_created,
                        subcategorydetails=att,
                        value=value
                    )
                print(timezone.now())


                image_instances = []
                for photo in image_files:
                    image_instance = Images(P=product_created, image=photo)
                    image_instances.append(image_instance)
                if image_instances:
                    Images.objects.bulk_create(image_instances)
                print(timezone.now())
              
                
                return Response({"message": "Data Saved", "product_id": product_created.id}, 
                              status=status.HTTP_201_CREATED)
                
        except Exception as e:
           
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in PutAd: {str(e)}")
            
            return Response(
                {"message": "An error occurred", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
class Updatedetails(APIView):
    http_method_names=['post']
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user=User.objects.get(id=request.user.id)
        data=request.data
        keys = [k for k in data.keys()]
        product_data={}
        title_data={}
        product_list=['id','category','subcategory','name','price','description','status','state','city','district','availabilty']
        for k in keys:
            if k in product_list:
                product_data[k]=data[k]
            else:
                title_data[k]=data[k]
        product_id = data.get('id') 
        product = get_object_or_404(Products, id=product_id) 
        for key, value in product_data.items():
            setattr(product, key, value)
        product.save()
        print(title_data)
        for key in title_data:
            product_subcategory_details = ProductSubcategoryDetails.objects.filter(Product_id=product_id)
            for pid in product_subcategory_details:
                subcat=pid.subcategorydetails
                print(subcat.title)
                if subcat.title==key:
                    pid.value=title_data[key]
                    pid.save()


        return Response({'message': 'Product updated successfully'})
    
class UserLikes(APIView):
    http_method_names=['post']
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        print(request.data)
        user=User.objects.get(id=data['id'])
        productdata=Products.objects.get(id=data['product_id'])
        if UserFavourites.objects.filter(product=productdata).exists():
            user=UserFavourites.objects.filter(product=productdata)
            user.delete()
            return Response({'msg':'Removed from Wishlist'})
        else:
            user_favourites=UserFavourites.objects.create(user=user,product=productdata)
            return Response({'msg':'Added in Favourites'})



def getoffset(page,limit):
    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * limit 
    return offset
            
# class displayAllAdView(generics.ListAPIView):
#     http_method_names = ['get']
    
    
#     # def list(self, request): http_method_names = ['get']
#     def list(self, request):
#         params=request.Get
#         try:
#             data=request.data
#             page=int(params('page',1))
#             limit=int(params('limit',2))
#             offset=getoffset(page,limit)

            
#             products=Products.objects.filter(availability="Sold")[offset:limit+offset]
#             # print(products)
#             product_list=displayAdSerializer(products,many=True)
#             product_data=product_list.data
#             return Response(data=product_data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"Error Occured":f"{e}"},status=status.HTTP_400_BAD_REQUEST)


# class displayAllAdView(generics.ListAPIView):
#     http_method_names = ['get']
   
    
#     def list(self, request):
#         try:
            
#             params = request.GET

#             page = int(params.get('page', 1))
#             limit = int(params.get('limit', 10))
#             offset=getoffset(page,limit)

#             # if page == 1:
#             #     offset = 0
#             # else:
#             #     offset = (page - 1) * limit 


#             id=request.user.id
#             queryset=Products.objects.all()[offset:limit + offset]
    
#             product_list=displayAdSerializer(queryset,many=True) 
#             product_data=product_list.data
#             # images=product_photos.objects.get(product=products.id)
#             return Response(data=product_data,status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"Error Occured":f"{e}"},status=status.HTTP_400_BAD_REQUEST)
class displayAllAdView(generics.ListAPIView):
    http_method_names = ['get']
    serializer_class = displayAdSerializer  
    pagination_class = None  

    def get_queryset(self):
        try:
            params = self.request.GET
            page = int(params.get('page', 1))
            if page<=0:
                page=1
            
            limit = int(params.get('limit', 30))
            # page = 1
            # limit = 10
            offset = getoffset(page, limit)

           
            queryset = Products.objects.all().order_by('-created_at')[offset:limit + offset]

            return queryset
        except Exception as e:
         
            print(f"Error in get_queryset: {e}")
            return Products.objects.none()  
    def list(self, request, *args, **kwargs):
        
        try:
           
            queryset = self.get_queryset()

         
            if not  request.user.is_authenticated:
                
                product_list=Logindisplayserializer(queryset,context = {'user':1},many=True)
                product_data = product_list.data
            else:
                product_list = displayAdSerializer(queryset, many=True)
               
                product_data = product_list.data

            
            return Response(data=product_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error Occurred": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)





class FindUserFavourites(APIView):
    http_method_names=['get']
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        params = request.GET
        print(params["id"])
        fav_info=UserFavourites.objects.filter(user=User.objects.get(id=int(params.get('id', 1))))
        serializer=UserFav(fav_info,many=True)
        data=serializer.data
        # data['is_favorite']=True
        return Response(data,status=status.HTTP_200_OK)

class Productdetail(APIView):
    http_method_names=['get']
    def get(self,request):
        params=self.request.GET
        id=params.get('id')
        try:
            product=Products.objects.get(id=id)
            image=list(Images.objects.filter(P=product))

            print(type(image))
            extra_image=namedtuple('image',['P','image'])
            image.insert(0,extra_image(image=product.display_photo,P=product))
           
            product_serializer=displayAdSerializer(product)
            image_serializer=DisplayImageSerializer(image,many=True)
            
            response_data = product_serializer.data
            response_data["images"] =  [img["image"] for img in image_serializer.data]
            
            return Response(data=response_data,status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({'msg':'Product not exist'},status=status.HTTP_404_NOT_FOUND) 
class ViewbyCategory(APIView):
    http_method_names = ['get']
    
    def get_queryset(self, category):
        try:
            params = self.request.GET
            page = int(params.get('page', 1))
            if page <= 0:
                page = 1

            limit = int(params.get('limit', 30))
            offset = getoffset(page, limit)

            return Products.objects.filter(
                category=category
            ).order_by('-created_at')[offset:limit + offset]
        except Exception as e:
            print(f"Error in get_queryset: {e}")
            return Products.objects.none()  

    def get(self, request):
        params = self.request.GET
        cat = params.get('category')
        # sub = params.get('subcategory')

        try:
            category = Category.objects.get(category_type=cat)
            # subcategory = Subcategory.objects.get(subcategory_nam)

           
            subcategory_counts = (
            Subcategory.objects
            .filter(U_id_id=category)  # Filtering by the provided category ID
            .annotate(product_count=Count('product_cat'))  # Counting related products
            .values('subcategory_name', 'product_count')
        )
            distinct_values = (
    ProductSubcategoryDetails.objects
    .filter(subcategorydetails__category_id=category, subcategorydetails__title='brand')
    .values_list("value", flat=True)
    .distinct()
)
            queryset = self.get_queryset(category)

            
            if not request.user.is_authenticated:
                product_list = Logindisplayserializer(queryset, context={'user': 1}, many=True)
            else:
                product_list = displayAdSerializer(queryset, many=True)

            product_data = {
                "products": product_list.data,  
                "subcategories": list(subcategory_counts),  
                "Brand":distinct_values
            }

            return Response(data=product_data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Subcategory.DoesNotExist:
            return Response({"error": "Subcategory not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Error occurred: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        
    


class Filters(APIView):
    http_method_names=['post']
    # authentication_classes=[JWTAuthentication]

    def post(self,request):
        try:
            data = request.data
            # data=data1['sampleData']
            
            category_name = data.get('category')
            
           
            subcategory_name = data.get('subcategory', None)

            filter_kwargs = {}

            if subcategory_name:
                filter_kwargs = {"subcategory_name":subcategory_name}
                
            brand = data.get('brand', [])
            price=data.get('price')
           

            min_price = price[0]
            max_price = price[1]
            
            
            current_year = datetime.now().year
            min_year = str(current_year - 15)
            max_year = str(current_year)

            if 'min_year' in data:
                min_year = str(data['min_year'])
            if 'max_year' in data:
                max_year = str(data['max_year'])

            
            try:
                category = Category.objects.get(category_type=category_name)

                if "subcategory_name" in filter_kwargs:
                    subcategory = Subcategory.objects.get( **filter_kwargs )

            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
            except Subcategory.DoesNotExist:
                return Response({"error": "Subcategory not found"}, status=status.HTTP_400_BAD_REQUEST)

            
            year_subquery = ProductSubcategoryDetails.objects.filter(
                subcategorydetails__category=category,
                subcategorydetails__subcategory=subcategory,
                subcategorydetails__title='year',
                value__range=(min_year, max_year)
            ).values_list('Product_id', flat=True)
            print(year_subquery)

            
            # brand_subquery = ProductSubcategoryDetails.objects.filter(
            #     subcategorydetails__category=category,
            #     subcategorydetails__subcategory=subcategory,
            #     subcategorydetails__title='brand',
            #     value__in=brand
            # ).values_list('Product_id', flat=True)
           

           # this query for to count the number of products of every subcatgory of particular category
            subcategory_counts = (
            Subcategory.objects
            .filter(U_id_id=category)  
            .annotate(product_count=Count('product_cat'))  
            .values('subcategory_name', 'product_count')
            )
            # this will find the brand names of this particular category
            distinct_values = (
            ProductSubcategoryDetails.objects
            .filter(subcategorydetails__category_id=category, subcategorydetails__title='brand')
            .values_list("value", flat=True)
            .distinct()
            )
           
            if not brand:
                brand = ProductSubcategoryDetails.objects.filter(
                    subcategorydetails__category=category,
                    subcategorydetails__subcategory=subcategory,
                    subcategorydetails__title='brand'
                ).values_list('value', flat=True)  
                print(brand)
            if isinstance(brand, str):
                brand = [brand]
            brand_subquery = ProductSubcategoryDetails.objects.filter(
            subcategorydetails__category=category,
            subcategorydetails__subcategory=subcategory,
            subcategorydetails__title='brand',
            value__in=brand
            ).values_list('Product_id', flat=True)
            
            print(brand_subquery)
            filtered_product_ids = set(year_subquery).intersection(set(brand_subquery))
            print(filtered_product_ids)
            products = Products.objects.filter(
    category=category,
    subcategory=subcategory,
    price__range=(min_price, max_price),
    id__in=filtered_product_ids  
)

            print(products)
            serialized_products =Logindisplayserializer(products, context={'user': 1}, many=True).data
            product_data = {
        "products": serialized_products,  
        "subcategories": list(subcategory_counts),  
        "Brand":distinct_values
    }

            return Response({"products": product_data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Filter2(APIView):
    http_method_names=['post']
    def get_queryset(self,Products):
        try:
            params = self.request.GET
            page = int(params.get('page', 1))
            if page<=0:
                page=1
            
            limit = int(params.get('limit', 30))
            # page = 1
            # limit = 10
            offset = getoffset(page, limit)
            if Products is None:
                queryset = Products.objects.all()
            
            queryset = Products.order_by('-created_at')[offset:limit + offset]

            return queryset
        except Exception as e:
            
            print(f"Error in get_queryset: {e}")
            return Products.objects.none()  
    def post(self,request):
        data=request.data
        category=data['category']
        subcategory=data.get('subcategory',None)
        brand=data.get('brand',[])
        price=data.get('price',[-1000,20000000])
        min_price = price[0]
        max_price = price[1]
            
       
        category=Category.objects.get(category_type=category)
        
        dbQuery = Products.objects.filter(category=category)

       
        dbQuery = dbQuery.filter(price__range=(min_price, max_price))

        
        if subcategory:
            subcategory=Subcategory.objects.get(subcategory_name=subcategory)
            dbQuery = dbQuery.filter(subcategory=subcategory)

        
        dbQuery = dbQuery.annotate(
            brand_value=Subquery(
                ProductSubcategoryDetails.objects.filter(
                    Product=OuterRef("id"),
                    subcategorydetails__title="brand"
                ).values("value") #[:1]
            )
        )
        print(dbQuery)

        
        if brand:
            
            if not isinstance(brand, list):
                brand = [brand]
            
            
            dbQuery = dbQuery.filter(brand_value__in=brand)
        else:
            
            available_brands = ProductSubcategoryDetails.objects.filter(
                subcategorydetails__category=category
            )
           
            if subcategory:
                available_brands = available_brands.filter(
                    subcategorydetails__subcategory=subcategory
                )
            available_brands = available_brands.filter(
                subcategorydetails__title="brand"
            ).values_list("value", flat=True).distinct()
            
            
            brand = available_brands

        
        products = dbQuery.distinct()
        queryset=self.get_queryset(products)
        
        subcategory_counts = (
            Subcategory.objects
            .filter(U_id_id=category)  
            .annotate(product_count=Count('product_cat'))  
            .values('subcategory_name', 'product_count')
            )
        distinct_values = (
            ProductSubcategoryDetails.objects
            .filter(subcategorydetails__category_id=category, subcategorydetails__title='brand')
            .values_list("value", flat=True)
            .distinct()
            )
        
        product_list =Logindisplayserializer(queryset, context={'user': 1}, many=True).data


        product_data = {
                "products": product_list,  
                "subcategories": list(subcategory_counts),  
                "Brand":distinct_values
            }

        return Response(data=product_data, status=status.HTTP_200_OK)
        



