# messages

``` python
def get_unread_notices(cookie):
def get_unread_replies(cookie,id_=None):
```

该库提供通知（点赞、回复）获取的功能
由于BAC文档未更新，本项目只提供了以上方法

#### 获取未读通知

> get_unread_notices(cookie)

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "at": 0,
        "coin": 0,
        "danmu": 0,
        "favorite": 0,
        "like": 0,
        "recv_like": 0,
        "recv_reply": 0,
        "reply": 0,
        "sys_msg": 0,
        "sys_msg_style": 1,
        "up": 0
    }
}
```

#### 获取回复

> get_unread_replies(cookie)

**由于返回过长，在这里把BAC的文档贴出来**

**json回复：**

根对象：

| 字段    | 类型 | 内容     | 备注                          |
| ------- | ---- | -------- | ----------------------------- |
| code    | num  | 返回值   | 0：成功<br />-101：账号未登录 |
| message | str  | 错误信息 | 默认为 0                      |
| ttl     | num  | 1        |                               |
| data    | obj  | 信息本体 |                               |

`data` 对象：

| 字段         | 类型  | 内容        | 备注                           |
| ------------ | ----- | ----------- | ------------------------------ |
| cursor       | obj   | 光标        | 下一次查询的指针               |
| items        | array | 通知列表    | 数组，每个元素代表一条回复通知 |
| last_view_at | num   | unix 时间戳 | 上次查看的时间                 |

`cursor` 对象：

| 字段   | 类型 | 内容        | 备注                                           |
| ------ | ---- | ----------- | ---------------------------------------------- |
| is_end | bool | 是否结束    | `false` 表示还有更多数据                       |
| id     | num  | 通知 id     | 最后（旧）一条通知的 id，用作下次查询的起始 id |
| time   | num  | unix 时间戳 | 最后一条通知的时间                             |

`items` 数组中的对象（每条通知）：

| 字段       | 类型 | 内容                 | 备注                         |
| ---------- | ---- | -------------------- | ---------------------------- |
| id         | num  | 通知 id              |                              |
| user       | obj  | **回复者**的用户信息 |                              |
| item       | obj  | 通知详情             |                              |
| counts     | num  | 通知计数             | 固定为 `1`，可能表示单条通知 |
| is_multi   | num  | 是否多回复           | 固定为 `0`，可能表示单条回复 |
| reply_time | num  | unix 时间戳          | 回复时间                     |

`user` 对象（回复者信息）：

| 字段     | 类型 | 内容           | 备注                           |
| -------- | ---- | -------------- | ------------------------------ |
| mid      | num  | 用户 mid       |                                |
| fans     | num  | 粉丝数         | 固定为 `0`，可能不返回实际数据 |
| nickname | str  | 用户昵称       |                                |
| avatar   | str  | 头像 URL       |                                |
| mid_link | str  | 用户主页链接   | 固定为空字符串                 |
| follow   | bool | 是否关注该用户 | `false` 表示未关注             |

`item` 对象（通知详情）：

| 字段                 | 类型  | 内容             | 备注                          |
| -------------------- | ----- | ---------------- | ----------------------------- |
| subject_id           | num   | 主体 id          |                              |
| root_id              | num   | 根评论 id        | 最顶层的评论 ID               |
| source_id            | num   | 源评论 id        | 直接回复的评论 ID             |
| target_id            | num   | 目标评论 id      | 被回复的评论 ID               |
| type                 | str   | 通知类型         | 固定为 `"reply"`（回复类型）  |
| business_id          | num   | 业务类型 id      | `1`=视频评论，`11`=动态评论   |
| business             | str   | 业务名称         | `"评论"` 或 `"视频"`          |
| title                | str   | 通知标题         | 摘要文本                      |
| desc                 | str   | 描述             | 固定为空字符串                |
| image                | str   | 图片 URL         | 固定为空字符串                |
| uri                  | str   | 跳转链接         | web 端跳转链接                |
| native_uri           | str   | 客户端跳转链接   | 客户端专用跳转链接            |
| detail_title         | str   | 详细标题         | 固定为空字符串                |
| root_reply_content   | str   | 根评论内容       | 最顶层评论的文本内容          |
| source_content       | str   | 源评论内容       | 直接回复的评论内容            |
| target_reply_content | str   | 目标评论内容     | 被回复的评论内容              |
| at_details           | array | @的用户列表      | 数组，每个元素是被@的用户对象 |
| topic_details        | array | 话题详情         | 固定为空数组                  |
| hide_reply_button    | bool  | 是否隐藏回复按钮 |                               |
| hide_like_button     | bool  | 是否隐藏点赞按钮 |                               |
| like_state           | num   | 点赞状态         | `0`=未点赞                    |
| danmu                | null  | 弹幕信息         | 固定为 `null`                 |
| message              | str   | 消息内容         | 固定为空字符串                |

`at_details` 数组中的对象（被@的用户）：

| 字段     | 类型 | 内容           | 备注               |
| -------- | ---- | -------------- | ------------------ |
| mid      | num  | 用户 mid       |                    |
| fans     | num  | 粉丝数         | 固定为 `0`         |
| nickname | str  | 用户昵称       |                    |
| avatar   | str  | 头像 URL       |                    |
| mid_link | str  | 用户主页链接   | 固定为空字符串     |
| follow   | bool | 是否关注该用户 | `false` 表示未关注 |

**示例：**

```shell
curl 'https://api.bilibili.com/x/msgfeed/reply' \
  -b 'SESSDATA=xxx'
```

<details>
<summary>查看响应示例：</summary>

```json
{
  "code": 0,
  "message": "0",
  "data": {
    "cursor": {
      "is_end": true,
      "id": 823260581625886,
      "time": 1749474709
    },
    "items": [{
      "id": 823260581625886,
      "user": {
        "mid": 3546910497441845,
        "fans": 0,
        "nickname": "佘总累了",
        "avatar": "https://i2.hdslb.com/bfs/face/e45c62bd47729e07dd01a788988be865ed3d210e.jpg",
        "mid_link": "",
        "follow": false
      },
      "item": {
        "subject_id": 1073543151725051921,
        "root_id": 0,
        "source_id": 265141324256,
        "target_id": 0,
        "type": "dynamic",
        "business_id": 17,
        "business": "动态",
        "title": "我已成为哔哩哔哩第245743680位转正会员，挑战转正答题考试获得60分。",
        "desc": "",
        "image": "",
        "uri": "https://www.bilibili.com/opus/1073543151725051921#reply265141324256",
        "native_uri": "bilibili://opus/detail/1073543151725051921?comment_root_id=265141324256&comment_on=1",
        "detail_title": "",
        "root_reply_content": "",
        "source_content": "60",
        "target_reply_content": "",
        "at_details": [],
        "topic_details": [],
        "hide_reply_button": false,
        "hide_like_button": false,
        "like_state": 0,
        "danmu": null,
        "message": ""
      },
      "counts": 1,
      "is_multi": 0,
      "reply_time": 1749474709
    }],
    "last_view_at": 1749474724
  }
}
```

</details>
