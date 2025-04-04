from django.urls import path,include
from .views import (
    Sellproduct,DisplayAdViewCategory,DisplayUsersAdView,
    FinDetails,PutAd,Updatedetails,UserLikes,displayAllAdView,
    FindUserFavourites,Productdetail,ViewbyCategory,
    Filters,Filter2
)

urlpatterns = [
    path('sellproduct/',Sellproduct.as_view(),name='sellproduct'),
    path("list/",DisplayAdViewCategory.as_view(),name="list_products"),
    # path("list/subcategory/",displayAdViewSubcategory.as_view(),name="list_products_subcategory"),
    path("ads/",DisplayUsersAdView.as_view(),name="users_products"),
    path("display/",FinDetails.as_view(),name="find_details"),
    path("putad/",PutAd.as_view(),name="Put_Ad"),
    path("updatedetails/",Updatedetails.as_view(),name="update_details"),
    path('userfavourites/',UserLikes.as_view(),name="User Favourites"),
    path('listall/',displayAllAdView.as_view(),name="display"),
    path('Favourites/',FindUserFavourites.as_view(),name="Favourites"),
    path('item/',Productdetail.as_view(),name="Detail"),
    path('getbycategory/',ViewbyCategory.as_view(),name="getbycat"),
    path('filters2/',Filters.as_view(),name="filters"),
    path('filters/',Filter2.as_view(),name="filters")

    



    
]
