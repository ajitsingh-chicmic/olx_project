from celery import shared_task
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.utils.timezone import now

@shared_task
def delete_expired_tokens():
    expired = OutstandingToken.objects.filter(expires_at__lt=now())
    count = expired.count()
    BlacklistedToken.objects.filter(token__in=expired).delete()
    expired.delete()
    return f"Deleted {count} expired tokens"