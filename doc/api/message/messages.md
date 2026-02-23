# messages

``` python
class private_unread_type:
    all_msg=0#全部
    only_follow=1#仅已关注
    only_unfollow=2#仅为关注
    only_dustbin=3#仅屏蔽，需show_dustbin
class session_type:
    private=1 #私聊
    group=2 #粉丝团
    
def get_unread_count_private(cookie,unread_type=private_unread_type.all_msg,show_unfollow_list=False,show_dustbin=False):
def get_unread_count_group(cookie):
def get_session_msgs(cookie,session_type,talker_id,size=0,begin_seqno='',end_seqno=''):
def send_message(cookie,message):
```

该库提供消息获取的功能

#### 获取未读私信数

> get_unread_count_private(cookie)

``` json
{
    "code":0,
    "msg":"0",
    "message":"0",
    "ttl":1,
    "data":{
        "unfollow_unread":1, #未读未关注用户消息
        "follow_unread":1, #未读已关注用户消息
        "unfollow_push_msg":0, #未读未关注用户推送
        "dustbin_push_msg":0, #未读被拦截推送
        "dustbin_unread":0, #未读被拦截消息
        "biz_msg_unfollow_unread":0, #未读未关注用户通知
        "biz_msg_follow_unread":1, #未读已关注用户通知
        "custom_unread":0 #未读客服消息
    }
}
```

#### 获取未读粉丝团消息数，返回简单明了

> get_unread_count_group(cookie)

``` json
{
    "code":0,
    "msg":"0",
    "message":"0",
    "ttl":1,
    "data":{
        "unread_count":0
    }
}
```

#### 获取指定对话的消息列表

> get_session_msgs(cookie,session_type.private,'12076317',1)
>
> size上限为2000
>
> begin_seqno,end_seqno代表返回以此id开始、结束的对话（不包括）

``` json
{
    "code": 0,
    "msg": "0",
    "message": "0",
    "ttl": 1,
    "data": {
        "messages": [
            {
                "sender_uid": 12076317,
                "receiver_type": 1,
                "receiver_id": 600189104,
                "msg_type": 1,
                "content": "{\"content\":\"你的账号在新设备或平台登录成功，如非本人操作，请及时修改密码（密码修改成功，全平台清空登录态）\\n设备/平台: Chrome浏览器\\n登录方式: 扫码登录\\n参考登录地: 中国湖北\\n登录时间: 2026-02-20 19:41:39\"}",
                "msg_seqno": 2279884386791433,
                "timestamp": 1771587699,
                "at_uids": [
                    0
                ],
                "msg_key": 7608911230016025338,
                "msg_status": 0,
                "notify_code": "3_13",
                "new_face_version": 1,
                "msg_source": 6
            },
            {
                "sender_uid": 12076317,
                "receiver_type": 1,
                "receiver_id": 600189104,
                "msg_type": 1,
                "content": "{\"content\":\"你的账号在新设备或平台登录成功，如非本人操作，请及时修改密码（密码修改成功，全平台清空登录态）\\n设备/平台: Edge浏览器\\n登录方式: 扫码登录\\n参考登录地: 中国湖北\\n登录时间: 2026-02-11 23:43:17\"}",
                "msg_seqno": 2267081676836864,
                "timestamp": 1770824598,
                "at_uids": [
                    0
                ],
                "msg_key": 7605633732095835976,
                "msg_status": 0,
                "notify_code": "3_13",
                "msg_source": 6
            }
        ],
        "has_more": 1,
        "min_seqno": 2267081676836864,
        "max_seqno": 2279884386791433
    }
}
```

#### 关于send_message,请见 [messageClass](./../../tools/class/message.md)