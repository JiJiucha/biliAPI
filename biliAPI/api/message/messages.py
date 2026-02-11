from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_private_unread_count
from biliAPI.tools.url import get_group_unread_count
from biliAPI.tools.url import get_messages_of_session,send_message_for_session

class private_unread_type:
    all_msg=0#全部
    only_follow=1#仅已关注
    only_unfollow=2#仅为关注
    only_dustbin=3#仅屏蔽，需show_dustbin
'''
type
1：用户与系统
2：未关注人
3：粉丝团
4：所有
5：被拦截
6：花火商单
7：所有系统消息
8：陌生人（与 “未关注人” 不同，不包含官方消息）
9：关注的人与系统
'''
'''
session_type:
1 私聊
2 粉丝团
'''
def get_unread_count_private(cookie,unread_type=0,show_unfollow_list=0,show_dustbin=0,build=0,mobi_app=0):
    return mrequests.get(get_private_unread_count,cookie=cookie,params={unread_type:unread_type,show_unfollow_list:show_unfollow_list,show_dustbin:show_dustbin,build:build,mobi_app:mobi_app})
    
def get_unread_count_group(cookie):
    return mrequests.get(get_group_unread_count,cookie=cookie)
    
def get_session_msgs(cookie,session_type,talker_id,size=0,begin_seqno='',end_seqno=''):
    return mrequests.get(get_messages_of_session,cookie=cookie,params={'talker_id':talker_id,'session_type':session_type,'size':size,'begin_seqno':begin_seqno,'end_seqno':end_seqno})

def send_message(cookie,message):
    return mrequests.post(send_message_for_session,cookie,withwbi=False,data=message.message)