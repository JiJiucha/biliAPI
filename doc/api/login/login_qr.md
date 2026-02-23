# login_qr

``` json
class login_qr_code:
    success=0 #成功登录
    invalid=86038 #二维码失效
    scan_but_no_confirm=86090 #已扫描但为确认
    unscan=86101 #未扫描

def generate_web():
def poll_web(key):
```

该库定义了二维码登录的相关方法（目前只支持网页端API）


#### 调用该方法申请登录，在手机端访问url可进行授权

> generate_web()

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "url": "https://passport.bilibili.com/h5-app/passport/login/scan?navhide=1\u0026qrcode_key=8587cf8106a0b863c46d6bab913537f6\u0026from=",
        "qrcode_key": "8587cf8106a0b863c46d6bab913537f6"
    }
}
```

#### 使用qrcode_key，通过poll_web进行轮询，可以获取登录状态
#### 确认登录成功后可以使用 [cookieClass.from_requests](./../../tools/class/cookie.md) 将请求对象传入来快速构建Cookie类

> poll_web(key)

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "url": "",
        "refresh_token": "",
        "timestamp": 0,
        "code": 86101,
        "message": "未扫码"
    }
}
```