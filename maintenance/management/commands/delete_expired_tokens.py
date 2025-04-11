from django.core.management.base import BaseCommand
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken ,OutstandingToken
from django.utils.timezone import now
class Command(BaseCommand):
    help='Delete expired tokens from BlacklistedToken and OutstandingToken tables'
    def handle(self,*args, **kwargs):
        expired=OutstandingToken.objects.filter(expires_at__lt=now())
        count=expired.count()
        BlacklistedToken.objects.filter(token__in=expired).delete()
        expired.delete()
        print("Deleted")

