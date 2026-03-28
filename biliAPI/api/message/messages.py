# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_unread_count_private_url
from biliAPI.tools.url import get_unread_count_group_url
from biliAPI.tools.url import get_session_msgs_url,send_message_url
from biliAPI.tools.cookie import cookieClass

class private_unread_type:
    all_msg=0#全部
    only_follow=1#仅已关注
    only_unfollow=2#仅为关注
    only_dustbin=3#仅屏蔽，需show_dustbin
class session_type:
    private=1 #私聊
    group=2 #粉丝团

def get_unread_count_private(cookie:cookieClass.Cookie,unread_type=private_unread_type.all_msg,show_unfollow_list=False,show_dustbin=False):
    return mrequests.get(get_unread_count_private_url,cookie=cookie,params={unread_type:unread_type,show_unfollow_list:(0 if show_unfollow_list else 1),show_dustbin:(0 if show_dustbin else 1)})
    
def get_unread_count_group(cookie:cookieClass.Cookie):
    return mrequests.get(get_unread_count_group_url,cookie=cookie)
    
def get_session_msgs(cookie:cookieClass.Cookie,session_type,talker_id,size=0,begin_seqno='',end_seqno=''):
    return mrequests.get(get_session_msgs_url,cookie=cookie,params={'talker_id':talker_id,'session_type':session_type,'size':size,'begin_seqno':begin_seqno,'end_seqno':end_seqno})

def send_message(cookie:cookieClass.Cookie,message):
    return mrequests.post(send_message_url,cookie,withwbi=False,data=message.message)