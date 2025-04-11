from django.urls import path,include
from .views import signupView ,loginView,decodejwt,LogoutView,ForgotpassView,changepassView,VerifyEmailView,editprofile,IsLogin,IsValidEmail,UpdateuserDetails,IsValidEmail,FindUserinfo
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('singup', include(account.urls))
    path('signup/',signupView.as_view(),name="signup"),
    path('login/',loginView.as_view(),name="Login"),
    path('decode/',decodejwt),
    path('logout/',LogoutView.as_view(),name='Logout'),
    # path('add/',makeentry.as_view(),name='make'),
    path('forgotpass/',ForgotpassView.as_view(),name='Forgotpassword'),
    path('changepass/',changepassView.as_view(),name='changepass'),
    path('emailverify/<uid>/<token>/',VerifyEmailView.as_view(),name='Emailverify'),
    path('editprofile/',editprofile.as_view(),name='editprofile'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sell/',IsLogin.as_view(),name="Is_login"),
    path('validemail',IsValidEmail.as_view,name="Valid Email"),
    path('updateuserdetails/',UpdateuserDetails.as_view(),name="user_detail_updation"),
    path('isvalidemail/',IsValidEmail.as_view(),name="Is_email_valid"),
    path('userinfo/',FindUserinfo.as_view(),name="user_info")



]