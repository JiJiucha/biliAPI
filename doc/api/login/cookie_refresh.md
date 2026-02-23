# cookie_refresh

``` python
def is_need_refresh(cookie)->BiliResponse:
def get_refresh_csrf(cookie)>str:
def refresh_cookie(cookie,refreshv_csrf,refresh_token)->BiliResponse:
def confirm_refresh_cookie(cookie,refresh_token)->BiliResponse:
```

该库提供刷新cookie的功能

### 过程示例：

#### 1.传入旧cookie判断是否需要刷新

> is_need_refresh(cookie)

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "refresh": false,
        "timestamp": 1684466082562
    }
}
```

#### 2.获取csrf
#### 原API的返回是一个网页，此处已解析，可直接使用返回

> get_refresh_csrf(cookie)

#### 3.确认刷新，可获取新的refresh_token，需手动保存至cookie

> refresh_cookie(cookie,csrf,token)

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "status": 0,
        "message": "",
        "refresh_token": "ae1bd1149b56af9743ffe7bbbeff3e51"
    }
}
```

#### 4.这里要传入新cookie与旧的refresh_token，使旧的refresh_token失效

> confirm_refresh_cookie(cookie,token)

``` json
{
    "code": 0,
    "message": "0",
    "ttl": 1
}
```

#### 关于自动刷新，可见 [refresh_helper](./../../tools/cookie/refresh_helper.md)