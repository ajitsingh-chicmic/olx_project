from django.db import models
from account.models import User
import uuid
from django.utils import timezone

# Create your models here.
class RoomInfo(models.Model):
    
    room_id=models.CharField(max_length=255, default=uuid.uuid4,unique=True)
    room_name=models.CharField(max_length=200)
    def __str__(self):
        return self.room_name
class GroupUser(models.Model):
    room_id=models.ForeignKey(RoomInfo,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.room_id
class MessageInfo(models.Model):
    room_id=models.ForeignKey(RoomInfo,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class ReadbyUser(models.Model):
    room_id=models.ForeignKey(RoomInfo,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    message_id=models.ForeignKey(MessageInfo,on_delete=models.CASCADE)
    readed=models.BooleanField(default=False)
    