from django.contrib.auth.models import AbstractBaseUser
# from django.db.models.manager import BaseManager,
from django.contrib.auth.models import BaseUserManager
import uuid
# Create your models here.
from django.db import models
from django.core.validators import RegexValidator



class MyUserManager(BaseUserManager):
    # obj.create_user('himanshu',)
    def create_user(self,username,email,password):
        
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email.lower(),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password):
        user = self.create_user(
        email=self.normalize_email(email),
        password=password,
        username=username,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    # def get_by_natural_key(self, email):
    #     # This is typically your unique field for the user model (like email or username)
    #     return self.get(email=email)

class User(AbstractBaseUser):
    # id = models.UUIDField(primary_key=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits long")],null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","password"]
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
# class mymodel(models.Model):
#          id=models.UUIDField(primary_key=True,default=uuid.uuid4)
#          email=models.EmailField()
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=200,null=True)
    age=models.IntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    about=models.TextField(null=True)
    phone_number=models.CharField(max_length=10,validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits long")])








