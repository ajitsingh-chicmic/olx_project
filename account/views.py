from django.shortcuts import render
from .models import User,UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import signupSerializer,LoginSerializer,forgotpassSerializer,changepassSerializer,emailVerifySerializer,editprofileSerializer,Userserializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from base64 import urlsafe_b64encode, urlsafe_b64decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from olx import settings
from django.shortcuts import get_object_or_404
from .permissions import isVerified
from django.db import transaction
from olx import settings
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
from django.core.mail import EmailMultiAlternatives
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        access_token=refresh.access_token
        # access_token['email']=user.email

        return {
            'refresh': str(refresh),
            'access': str(access_token),
        }


class signupView(APIView):
    http_method_names=['post']
    
    def post(self,request):
        with transaction.atomic():
            
            data=request.data
            serializer=signupSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user=User.objects.get(email=serializer.validated_data['email'])
                uid=urlsafe_b64encode(force_bytes(user.email))
            
                token=default_token_generator.make_token(user)
                url=request._current_scheme_host+'/account/'+'emailverify'+'/'+uid.decode('utf-8') +'/'+token
                subject = "Verify Your Email"
                to_email = user.email

                text_content = f"Please verify your email by clicking this link: {url}"

                html_content = f"""
                <html>
                    <body>
                        <p>Click the button below to verify your email:</p>
                        <a href="{url}" style="
                            display: inline-block;
                            padding: 10px 20px;
                            font-size: 16px;
                            color: white;
                            background-color: #007BFF;
                            text-decoration: none;
                            border-radius: 5px;
                        ">Verify Email</a>
                        <p>If the button doesn't work, you can also click on  this link:</p>
                        <p><a href="{url}">{url}</a></p>
                    </body>
                </html>
                """

                email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()

                return Response({"message":"Created Succussfully"},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
from rest_framework_simplejwt.views import TokenBlacklistView


class loginView(APIView):
   http_method_names=['post']
   permission_classes=[isVerified]
   
   def post(self,request): 
        data=request.data
        if not data:
                return Response({"detail":"Email not found "},status=status.HTTP_401_UNAUTHORIZED)
       
        serializer=LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
           
            # if not data:
            #     return Response({"msg":"Email not found "},status=status.HTTP_401_UNAUTHORIZED)
            if not user:
                return Response({'detail':'Password not matched '},status=status.HTTP_401_UNAUTHORIZED)
            else:
                token=get_tokens_for_user(user)
                token['username']=user.username
                token['id']=user.id
                return Response(token,status=status.HTTP_200_OK)
        else:
             return Response({"detail":"Email not found "},status=status.HTTP_402_PAYMENT_REQUIRED)

def decodejwt(request):
     header=request.header.get('Authentication').split(' ')[1]
    #  header.de
     print(header)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken


class LogoutView(APIView):
    http_method_names = ['post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    
    def post(self, request):
       
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return Response({"detail": "Authorization header missing."}, status=400)

        try:
           
            access_token = authorization_header.split(' ')[1]

           
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response({"detail": "Refresh token is required in the request body."}, status=400)

          
            refresh_token_obj = RefreshToken(refresh_token)

            
            refresh_token_obj.blacklist()

            return Response({"detail": "Successfully logged out."}, status=200)

        except IndexError:
            return Response({"detail": "Invalid access token format."}, status=400)
        except InvalidToken:
            return Response({"detail": "Invalid token."}, status=400)
        # return Response('Logged Out ')

# def makeentry(request):
#     user=mymodel.objects.create_user(email='ajitrana515@gmail.com')
#     return HttpResponse('Created')

# class makeentry(APIView):
#     http_method_names=['post']
#     def post(self,request):
#         user=mymodel.objects.create(email=request.data.get("email"))
#         return Response('Created')
class ForgotpassView(APIView):
    http_method_names=['post']
    def post(self,request):
        data=request.data
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        else:
            serializer=forgotpassSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                email=serializer.validated_data['email']
                user=User.objects.get(email=email)
                uid=urlsafe_b64encode(force_bytes(user.id))
                subject = "Email For Password Change"
            
                token=default_token_generator.make_token(user)
                url = f"{settings.FRONTEND_BASE_URL}newpassword/{uid.decode('utf-8')}/{token}"
                text_content = f"Please change your password  by clicking this link: {url}"

                html_content = f"""
                <html>
                    <body>
                        <p>Click the button below to change your password:</p>
                        <a href="{url}" style="
                            display: inline-block;
                            padding: 10px 20px;
                            font-size: 16px;
                            color: white;
                            background-color: #007BFF;
                            text-decoration: none;
                            border-radius: 5px;
                        ">Change  Password</a>
                        <p>If the button doesn't work, you can also click on  this link:</p>
                        <p><a href="{url}">{url}</a></p>
                    </body>
                </html>
                """
                to_email = user.email
                email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()

                
                return Response({'msg':'Link Sent successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'Errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        

class changepassView(APIView):
    http_method_names=['post']
    def post(self,request):
        data=request.data
        uid=data['id']
        token=data['token']
       
        decoded_bytes = urlsafe_b64decode(uid)
        decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
        uid=int(decoded_string)
        user = get_object_or_404(User, id=uid) 
        if default_token_generator.check_token(user,token):
            
            
            print(user.id)
            print(token)
            user.set_password(data['password'])
            user.last_login=timezone.now()
            user.save()
            return Response({'msg':'Password Changed Successfully'},status=status.HTTP_200_OK)
        
        return Response("Link Expired ") 
        
class VerifyEmailView(APIView):
    http_method_names=['get']
    def get(self,request,uid,token):
        decoded_bytes = urlsafe_b64decode(uid)
        email = decoded_bytes.decode('utf-8', errors='ignore')
       
        
        user=User.objects.get(email=email)
        if user.is_verified==1:
            return Response({'msg:Email Already Verified'},status=status.HTTP_200_OK)
        if default_token_generator.check_token(user,token):

        
            user.is_verified=1
            user.save()
            return Response({'msg':'Email Verified Successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'Link is invalid '},status=status.HTTP_404_NOT_FOUND)
class editprofile(APIView):
    http_method_names=['post']
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        # print(data)
        # print(type(data))
        # # print(data['user'])
        # print(request.user.id)
        data['user']=request.user.id
        print(data['user'])
        user=request.user.id

        serializer=editprofileSerializer(data=data)
        with transaction.atomic():
            if serializer.is_valid():
                if 'email' in   data['email']:
                    user['email']=data ['email']
                if 'phone_number' in data['phone_number']:
                    user['phonenumber']=data['phone_number']
                serializer.save()
                return Response({'msg':'Data Saved Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Some error occured '},status=status.HTTP_400_BAD_REQUEST)
class IsLogin(APIView):
    http_method_names=['get']
    authentication_classes=[JWTAuthentication]
    permission_classes=[AllowAny]
    def get(self,request):
        if request.user.is_authenticated:
            return Response({'msg':'User is allowed to sell '},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'User not allowed to sell the product'},status=status.HTTP_401_UNAUTHORIZED)
class IsValidEmail(APIView):
    http_method_names=['post']
    def post(self,request):
        data=request.data
        email=data['email']
        if User.objects.filter(email=email).exists():
            return Response({'msg':'Email Already Exist in the database'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':"Email is available for modification"},status=status.HTTP_200_OK)

class UpdateuserDetails(APIView):
    http_method_names = ['post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        user_fields = ['username', 'phonenumber', 'email']

        for key in user_fields:
            if key in data:
                setattr(user, key, data[key])
        user.save()

        if 'about' in data:
            profile = UserProfile.objects.filter(user=user).first()
            if profile:
                profile.about = data['about']
                profile.save()
        if 'email' in data:
            uid=urlsafe_b64encode(force_bytes(user.email))
            
            token=default_token_generator.make_token(user)
            url=request._current_scheme_host+'/account/'+'emailverify'+'/'+uid.decode('utf-8') +'/'+token
            subject = "Verify Your Email"
            to_email = user.email

            text_content = f"Please verify your email by clicking this link: {url}"

            html_content = f"""
            <html>
                <body>
                    <p>Click the button below to verify your email:</p>
                    <a href="{url}" style="
                        display: inline-block;
                        padding: 10px 20px;
                        font-size: 16px;
                        color: white;
                        background-color: #007BFF;
                        text-decoration: none;
                        border-radius: 5px;
                    ">Verify Email</a>
                    <p>If the button doesn't work, you can also click on  this link:</p>
                    <p><a href="{url}">{url}</a></p>
                </body>
            </html>
            """

            email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()
            return Response({"message": "User details updated successfully."},status=status.HTTP_200_OK)


        return Response({"message": "User details updated successfully."})

class FindUserinfo(APIView):
    http_method_names=['get']
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        print(user)
        user_info=Userserializer(user).data
        if UserProfile.objects.filter(user=user).exists():
            p=UserProfile.objects.get(user=user)
        
            user_info['about']=p.about
        
        
        return Response(data=user_info,status=status.HTTP_200_OK)




