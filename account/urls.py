from django.urls import path,include
from .views import signupView ,loginView,decodejwt,LogoutView,ForgotpassView,changepassView,VerifyEmailView,editprofile

urlpatterns = [
    # path('singup', include(account.urls))
    path('signup/',signupView.as_view(),name="signup"),
    path('login/',loginView.as_view(),name="Login"),
    path('decode/',decodejwt),
    path('logout/',LogoutView.as_view(),name='Logout'),
    # path('add/',makeentry.as_view(),name='make'),
    path('forgotpass/',ForgotpassView.as_view(),name='Forgotpassword'),
    path('changepass/<uid>/<token>/',changepassView.as_view(),name='changepass'),
    path('emailverify/<uid>/<token>/',VerifyEmailView.as_view(),name='Emailverify'),
    path('editprofile/',editprofile.as_view(),name='editprofile')

]