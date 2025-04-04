from django.contrib import admin
from .models import RoomInfo,MessageInfo,GroupUser,ReadbyUser

# Register your models here.
@admin.register(RoomInfo)
class adminRoom(admin.ModelAdmin):
    list_display=['room_id','room_name']
@admin.register(MessageInfo)
class adminMessage(admin.ModelAdmin):
    list_display=['room_id','user_id','message','created_at']
@admin.register(GroupUser)
class adminGroup(admin.ModelAdmin):
    list_display=['room_id','user_id']
@admin.register(ReadbyUser)
class adminGroup(admin.ModelAdmin):
    list_display=['id','room_id','user_id','message_id']

