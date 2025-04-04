from django.shortcuts import render
from .models import User,UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import signupSerializer,LoginSerializer,forgotpassSerializer,changepassSerializer,emailVerifySerializer,editprofileSerializer
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

# Create your views here.

from rest_framework_simplejwt.tokens import RefreshToken

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
        data=request.data
        serializer=signupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.get(email=serializer.validated_data['email'])
            uid=urlsafe_b64encode(force_bytes(user.email))
        
            token=default_token_generator.make_token(user)
            url=request._current_scheme_host+'/account/'+'emailverify'+'/'+uid.decode('utf-8') +'/'+token
            subject="Your Verification link is :"
            message=url
            email=serializer.validated_data['email']
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
            return Response({"message":"Created Succussfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
from rest_framework_simplejwt.views import TokenBlacklistView


class loginView(APIView):
   http_method_names=['post']
   permission_classes=[isVerified]
   
   def post(self,request): 
        data=request.data
       
        serializer=LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
           
            if not data:
                return Response({"msg":"Password not matched "},status=status.HTTP_401_UNAUTHORIZED)
            elif not user:
                return Response({'msg':'Not Valid Email'},status=status.HTTP_401_UNAUTHORIZED)
            else:
                token=get_tokens_for_user(user)
                return Response(token,status=status.HTTP_200_OK)
        else:
             return Response('some error occured',status=status.HTTP_402_PAYMENT_REQUIRED)

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
        serializer=forgotpassSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.validated_data['email']
            user=User.objects.get(email=email)
            uid=urlsafe_b64encode(force_bytes(user.id))
        
            token=default_token_generator.make_token(user)
            url=request._current_scheme_host+'/account/'+'changepass/'+uid.decode('utf-8') +'/'+token
            subject="Your Verification link is :"
            
        
            message=url
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
            return Response({'msg':'Link Sent successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'Errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
class changepassView(APIView):
    http_method_names=['post']
    def post(self,request,uid,token):
        data=request.data
        serializer=changepassSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            decoded_bytes = urlsafe_b64decode(uid)
            decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
            uid=int(decoded_string)
            user = get_object_or_404(User, id=uid) 
            if default_token_generator.check_token(user,token):
                
                print(serializer.validated_data['password'])
                print(user.id)
                print(token)
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({'msg':'Password Changed Successfully'},status=status.HTTP_200_OK)
            return Response("Token invalid") 
        else:
            return Response({'errors':serializer.errors},status=status.HTTP_200_OK)
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
            return Response({'Error':'Email Not Verified'},status=status.HTTP_404_NOT_FOUND)
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

        serializer=editprofileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Saved Successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'msg':'Some error occured '},status=status.HTTP_400_BAD_REQUEST)

        