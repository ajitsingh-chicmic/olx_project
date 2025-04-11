from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User,MyUserManager,UserProfile
from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model


class signupSerializer(ModelSerializer):
   
    class Meta:
        model=User
        fields=["username","email","password"]
            
    # def validate(self, attrs):
    #     password1=attrs.get("password")
    #     password2=attrs.get("password2")
    #     if password1!=password2:
    #         raise ValidationError("Confirm password and password must be same")
    #     return attrs
    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)  # Corrected: Use the manager's create_user method
        return user


from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User  # Assuming User model is located in your app

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        
        email = attrs.get('email')
        password = attrs.get('password')
        

        if not email or not  password:
            
            
            
                
            raise serializers.ValidationError("Invalid email or password.")
            
            
        else:
            
            return attrs
class forgotpassSerializer(serializers.Serializer):
    email=serializers.EmailField()
    class Meta:
        Model=User
        fields=['email','password']
        def validate(self,attrs):
            email=attrs.get('email')
            try:
                user=User.objects.get(email=email)
               
            except User.DoesNotExist:
                raise ValidationError('User not Exist')
            return attrs
class changepassSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True)     
    conf_password=serializers.CharField(write_only=True) 
    class Meta:
        Model=User
        fields=['email','pass']
        def validate(self,attrs):
            password=attrs.get('password1')
            conf_password=attrs.get('password2')
            if password!=conf_password:
                raise ValidationError('Both Passwords must be Same')
            else:
                return attrs

class emailVerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    class Meta:
        Model=User
        fields=['email']
    def validate(self, attrs):
        email=attrs.get('email')
        

        return super().validate(attrs)
from rest_framework import serializers
from .models import UserProfile

class editprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'age', 'date_of_birth', 'about', 'phone_number']
    
    def create(self, validated_data):
        if UserProfile.objects.filter(user=validated_data['user']).exists():
            user=UserProfile.objects.filter(user=validated_data['user'])
            user.delete()
        return UserProfile.objects.create(**validated_data)
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','phonenumber','is_verified']
            

         
        

        
