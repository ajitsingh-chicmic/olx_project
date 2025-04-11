from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import User

class isVerified(BasePermission):
    def has_permission(self, request, view):
        email=request.data['email']
        try:
            user2=User.objects.get(email=email)


            return bool(request.user and user2.is_verified==1)
        except User.DoesNotExist:
            raise PermissionDenied("User not found or unauthorized.")
        except :
            raise PermissionDenied("Your email is not verified please verify it")