from django.db.models import Count
import jwt
from olx.settings import sio
from jwt.exceptions import InvalidTokenError
from channels.db import database_sync_to_async
from .utilites import get_or_create_room
from .models import User,RoomInfo,GroupUser,MessageInfo,ReadbyUser
SECRET_KEY = 'django-insecure-5b3j8^=-lo8^#2stmf95!5)$i3c$2zrhromjyivy!un)%w#wn#'
@database_sync_to_async
def save_msg(room_id,user_id,msg):
    room_id=RoomInfo.objects.get(id=room_id)
    user_id=User.objects.get(id=user_id)
    message=MessageInfo.objects.create(room_id=room_id,user_id=user_id,message=msg)

    return message
@database_sync_to_async
def save_room(room,user,message,is_online):
    
    room=RoomInfo.objects.get(id=room)
    
    room1=ReadbyUser.objects.create(room_id=room,user_id=user,message_id=message,readed=is_online)
    return room1
@database_sync_to_async
def get_other_user(room_id, sender):
    user = GroupUser.objects.filter(room_id=room_id).exclude(user_id=sender).first()
    user1=User.objects.get(email=user.user_id)
    return {"id": user1.id, "user_id": user1.email} if user else None
@database_sync_to_async
def verify_token(token):
   
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        # print(decoded)
        return decoded  
    except InvalidTokenError:
        return None
@database_sync_to_async
def get_unread_messages(user_id):
    return list(
        ReadbyUser.objects.filter(user_id=user_id)
        .values("room_id")
        .annotate(count=Count("id"))
    )
@database_sync_to_async
def get_userinfo(user):
    return User.objects.get(id=user)
@database_sync_to_async
def create_room1(user1,user2):
    return  RoomInfo.objects.create(room_name=f'{user1.username}-{user2.username}')
@database_sync_to_async
def groupuser(room,user1,user2):
    g1=GroupUser.objects.create(room_id=room,user_id=user1)
    g2= GroupUser.objects.create(room_id=room,user_id=user2)
    g1.save()
    g2.save()
def is_user_in_room(sid, room):
    # print(f"Checking if SID {sid} is in room {room}")
    try:
        rooms = sio.rooms(sid)
        # print(f"Rooms for SID {sid}: {rooms}")
        return room in rooms
    except Exception as e:
        # print(f"Exception in is_user_in_room: {e}")
        return False
@database_sync_to_async
def get_messages_by_room_and_user(room_id, user_id):
    return list(
        ReadbyUser.objects.filter(room_id=room_id, user_id=user_id)
        .select_related('message_id')
        .values('message_id__message')
    )

from django.db.models import Max

@database_sync_to_async
def get_latest_messages(user_id):
  
    user_rooms = GroupUser.objects.filter(user_id=user_id).values_list('room_id', flat=True)

   
    latest_messages = (
        MessageInfo.objects.filter(room_id__in=user_rooms)
        .values('room_id')
        .annotate(latest_message=Max('created_at')) 
    )

 
    messages = MessageInfo.objects.filter(
        room_id__in=user_rooms,
        created_at__in=[msg['latest_message'] for msg in latest_messages]
    ).values('room_id', 'message')

    return list(messages)
