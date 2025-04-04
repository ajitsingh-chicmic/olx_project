from rest_framework.permissions import BasePermission
from .models import User
class isVerified(BasePermission):
    def has_permission(self, request, view):
        email=request.data['email']
        try:
            user2=User.objects.get(email=email)


            return bool(request.user and user2.is_verified==1)
        except :
            return  False