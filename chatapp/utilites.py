from .models import RoomInfo,GroupUser,MessageInfo
from django.db.models import Q

def get_or_create_room(sender,reciever):
    room = RoomInfo.objects.filter(
    Q(groupuser__user_detail=sender) & Q(groupuser__user_detail=reciever)
).first()
    if not room:
        room = RoomInfo.objects.create(room_name=f"{sender.username} - {reciever.username}")
        GroupUser.create(room_detail=room,user_id=sender.username)
        GroupUser.create(room_detail=room,user_id=sender.username)
    return room