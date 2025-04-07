from olx.settings import sio
from django.db.models import Count
import json
from asgiref.sync import sync_to_async
# from asgiref.sync import database_sync_to_async
from channels.db import database_sync_to_async
from .utilites import get_or_create_room
from .models import User,RoomInfo,GroupUser,MessageInfo,ReadbyUser
import jwt
from jwt.exceptions import InvalidTokenError
from urllib.parse import parse_qs
import asyncio
from chatapp import helper_func as func



# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
so = sio


user_conn ={}
result={}


@so.event
async def connect(sid,environ,auth=None):
    print('connecteddeddede',sid)
    query_string = environ.get('QUERY_STRING')
    query_params = parse_qs(query_string)
    token = query_params.get('authorization', None)
    # print(token)
   
    
    user=await func.verify_token(token[0])
    if not user:
        print("Invalid token, disconnecting user.")
        await so.disconnect(sid)
        return
    
   
    user_conn[user['user_id']]=sid
   
   
   
    
    await so.save_session(sid, {"user_id": user['user_id'], "unread_messages": result})
    
   
    await so.emit('connected',{"message":"Hi", "sid": sid}, to = sid)
    await so.emit('abcb', 'dsbchd')
    
@so.on('disconnect')
async def disconnect(sid):
    print(f"Disconnecting SID: {sid}")
    
   
    session_data = await so.get_session(sid)
    user_id = session_data.get("user_id")

    
    if user_id in user_conn:
        user_conn.pop(user_id, None)

    # Leave all rooms
    for room in sio.rooms(sid):
        await sio.leave_room(sid, room)

    


# socket events
@so.on('event_name')
async def event_name(sid, data):

    data = json.loads(data)
    await so.emit('emitted_event',{"data": data['data']}, to = sid)
@so.on('create_room')
async def  create_room(sid,data):
    # print(type(data))
    
    sender=data['sender']
    # print(sender)
    reciever=data['receiver']
   
    user1=await func.get_userinfo(sender)
    user2=await func.get_userinfo(reciever)
  
    room_name = f'{user1.username}-{user2.username}'
    existing_room = await RoomInfo.objects.filter(room_name=room_name).afirst()
    if existing_room:
        data=existing_room.id 

    else:
        room=await func.create_room1(user1,user2)
        await func.groupuser(room,user1,user2)

        data['room_id']=room.id
    await so.emit('roomnumber_created',{"data":data},to=sid)    


@so.on('send_mesg')
async def send_mesg(sid,data):
    # print('in send message')
    sender=data['sender']
    room_id=data['room_id']
    # data=json.loads(data)
    msg=data['msg']
    
    await  sio.enter_room(sid=sid,room=room_id)
    message=await func.save_msg(room_id,sender,msg)
    message_response={
        'sender_id':sender,
        'room_id':room_id,
        'message':msg,
        'time': message.created_at.isoformat()

    }
    other_user = await func.get_other_user(room_id, sender)   
    # print(other_user['id'])
    
    # print(other_user)
    # print(user_conn)
    

    try:
        # print(other_user.user_id)
        is_user_online=func.is_user_in_room(user_conn[other_user['id']],room_id)
        
        
        online=False
        if is_user_online:
            print('User is online')
            online=True
        else:
          
            user=await func.get_userinfo(other_user['id'])
            room1=await func.save_room(room_id,user,message,online)
    except Exception as e:
        print('User is offline ')
    

    await so.emit('received_msg',message_response,room=room_id)
    
@so.on('join_room')
async def join_room(sid,data):

    room_id=data['room_id']
    for room in sio.rooms(sid):
         if room != sid:
            await sio.leave_room(sid, room)
    await sio.enter_room(sid=sid,room=room_id)
   
    messages=await func.get_all_message(room_id)
    session_data=await so.get_session(sid)
    user_id=session_data.get('user_id')
    print(user_id)
    await func.readed_by_user(room_id,user_id)

    await so.emit('retrieve',{"mesages":messages},to=sid)
   

    


@so.on('unread_message')
async def unread(sid,data):
    session_data = await so.get_session(sid)  # Retrieve session data
    user_id=session_data.get("user_id")
    result=await func.get_unread_messages(user_id)
    latest_messages = await func.get_latest_messages(user_id)
    
    await so.emit('maxi', {
        "unread_messages": result,
        "latest_messages": latest_messages
    }, to=sid)

    
@so.on('get_all_unread')
async def unread(sid,data):
    room_id=data['room_id']
    session_data=await sio.get_session(sid)
    user_id=session_data.get("user_id") 
    text=await func.get_messages_by_room_and_user(room_id,user_id)
    await so.emit('unreadmessagetext',{"message": text},to=sid)










    







