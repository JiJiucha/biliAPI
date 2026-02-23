# nav导航信息

```python
def get_nav_info(cookie=cookieClass.null_cookie):
```

#### 登录状态：

<details>
<summary>已折叠</summary>

``` json
{
    "code": 0,
    "message": "OK",
    "ttl": 1,
    "data": {
        "isLogin": true,
        "email_verified": 1,
        "face": "https://i2.hdslb.com/bfs/face/977c6f1128f0099a9cc5cba93c2916151cf9a8b5.jpg",
        "face_nft": 0,
        "face_nft_type": 0,
        "level_info": {
            "current_level": 5,
            "current_min": 10800,
            "current_exp": 17305,
            "next_exp": 28800
        },
        "mid": 600189104,
        "mobile_verified": 1,
        "money": 940.1,
        "moral": 70,
        "official": {
            "role": 0,
            "title": "",
            "desc": "",
            "type": -1
        },
        "officialVerify": {
            "type": -1,
            "desc": ""
        },
        "pendant": {
            "pid": 3144,
            "name": "原神",
            "image": "https://i2.hdslb.com/bfs/garb/item/6d5969a4f02fa1d4e5776072dc9f0b006478e82b.png",
            "expire": 0,
            "image_enhance": "https://i2.hdslb.com/bfs/garb/item/ff5bde4a6337140b632beffd0cbbaaf927c03ac0.webp",
            "image_enhance_frame": "https://i2.hdslb.com/bfs/garb/item/a1893352f03d1d6b321d504ba2ae0ecc0ea85647.png",
            "n_pid": 3144
        },
        "scores": 0,
        "uname": "鸡久叉",
        "vipDueDate": 1712937600000,
        "vipStatus": 0,
        "vipType": 1,
        "vip_pay_type": 0,
        "vip_theme_type": 0,
        "vip_label": {
            "path": "",
            "text": "",
            "label_theme": "",
            "text_color": "",
            "bg_style": 0,
            "bg_color": "",
            "border_color": "",
            "use_img_label": true,
            "img_label_uri_hans": "",
            "img_label_uri_hant": "",
            "img_label_uri_hans_static": "https://i0.hdslb.com/bfs/vip/d7b702ef65a976b20ed854cbd04cb9e27341bb79.png",
            "img_label_uri_hant_static": "https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/KJunwh19T5.png",
            "label_id": 0,
            "label_goto": null
        },
        "vip_avatar_subscript": 0,
        "vip_nickname_color": "",
        "vip": {
            "type": 1,
            "status": 0,
            "due_date": 1712937600000,
            "vip_pay_type": 0,
            "theme_type": 0,
            "label": {
                "path": "",
                "text": "",
                "label_theme": "",
                "text_color": "",
                "bg_style": 0,
                "bg_color": "",
                "border_color": "",
                "use_img_label": true,
                "img_label_uri_hans": "",
                "img_label_uri_hant": "",
                "img_label_uri_hans_static": "https://i0.hdslb.com/bfs/vip/d7b702ef65a976b20ed854cbd04cb9e27341bb79.png",
                "img_label_uri_hant_static": "https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/KJunwh19T5.png",
                "label_id": 0,
                "label_goto": null
            },
            "avatar_subscript": 0,
            "nickname_color": "",
            "role": 0,
            "avatar_subscript_url": "",
            "tv_vip_status": 0,
            "tv_vip_pay_type": 0,
            "tv_due_date": 0,
            "avatar_icon": {
                "icon_resource": {}
            },
            "ott_info": {
                "vip_type": 1,
                "pay_type": 0,
                "pay_channel_id": "",
                "status": 0,
                "overdue_time": 1594137600
            },
            "super_vip": {
                "is_super_vip": false
            }
        },
        "wallet": {
            "mid": 600189104,
            "bcoin_balance": 0,
            "coupon_balance": 0,
            "coupon_due_time": 0
        },
        "has_shop": false,
        "shop_url": "",
        "answer_status": 0,
        "is_senior_member": 0,
        "wbi_img": {
            "img_url": "https://i0.hdslb.com/bfs/wbi/7cd084941338484aae1ad9425b84077c.png",
            "sub_url": "https://i0.hdslb.com/bfs/wbi/4932caff0ff746eab6f01bf08b70ac45.png"
        },
        "is_jury": false,
        "name_render": null,
        "legal_region": "CN",
        "ip_region": "CN"
    }
}
```

</details>

#### 未登录状态：

``` json
{
    "code": -101,
    "message": "账号未登录",
    "ttl": 1,
    "data": {
        "isLogin": false,
        "wbi_img": {
            "img_url": "https://i0.hdslb.com/bfs/wbi/653657f524a547ac981ded72ea172057.png",
            "sub_url": "https://i0.hdslb.com/bfs/wbi/6e4909c702f846728e64f6007736a338.png"
        },
    }
}
```

可见是否登录不会影响wbi获取