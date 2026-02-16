# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

import uuid,time,json

class private_msg_type:
    text=1
    img=2
    recall=5
    emoji=6
    share=7
    mini_app=9
    notice=10
    video_push=11
    column_push=12
    img_card=13
    other_share=14
    push_on_follow=16
    sys_notice=18
class group_msg_type:
    on_join=301
    on_leave=302
    group_display=303
    group_dismiss=304
    group_create=305
    on_join2=306

class Message:
    
    def __init__(self,cookie,session_type,receiver,content):
        self.message={
            'msg[msg_status]':0,
            'mobi_app':0
        }
    
        dev_id = str(uuid.uuid4())
        
        self.message['msg[sender_uid]']=cookie.get('DedeUserID')
        self.message['msg[receiver_id]']=receiver
        self.message['msg[receiver_type]']=session_type
        self.message['msg[msg_type]']=content.msg_type
        self.message['msg[timestamp]']=round(time.time())
        self.message['msg[content]']=json.dumps(content.content)
        self.message['msg[dev_id]']=dev_id
        
        
        self.message['csrf_token']=cookie.get('bili_jct')
        self.message['csrf']=cookie.get('bili_jct')
class MessageContentText:
    msg_type=1
    def __init__(self,text):
        self.content={'content':str(text)}
class MessageContentImage:
    msg_type=2
    def __init__(self,img_url,original=False,height=None,width=None):
        self.content={'url':img_url}
        if height!=None:
            self.content['height']=height
        if width!=None:
            self.content['width']=width
        if original:
            self.content['original']=1
class MessageContentRecall:
    msg_type=5
    def __init__(self,msg_key):
        self.content=msg_key
