# biliAPI库
<!--<p align="center" class="shields">
    <a href="https://github.com/JiJiucha/biliAPI/issues" style="text-decoration: none;">
        <img src="https://img.shields.io/github/issues/JiJiucha/biliAPI.svg?style=flat&color=red" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/JiJiucha/biliAPI/stargazers" style="text-decoration: none;">
        <img src="https://img.shields.io/github/stars/JiJiucha/biliAPI.svg?style=flat&color=yellow" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/JiJiucha/biliAPI/network" style="text-decoration: none;">
        <img src="https://img.shields.io/github/forks/JiJiucha/biliAPI.svg?style=flat&color=blue" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/JiJiucha/biliAPI/blob/master/LICENSE" style="text-decoration: none;">
        <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat" alt="GitHub license"/>
    </a>
</p>-->
<center>biliAPI库提供了使用Python访问B站API的便捷功能</center>
<center>旨在使开发者便捷的实现所需的功能</center>

## 文档导航

<details>
<summary>项目树状图</summary>

```text
biliAPI/
|----api/
|    |----login/
|    |    |----buvid.py
|    |    |----cookie_refresh.py
|    |    |----login_qr.py
|    |    |----logout.py
|    |    |----nav.py
|    |----message/
|    |    |----messages.py
|    |    |----notice.py
|    |    |----session.py
|    |----my_info/
|    |    |----my_info.py
|    |    |----sign.py
|    |    |----vip.py
|    |----safety/
|    |    |----account_info.py
|    |    |----base_info.py
|    |    |----bili_ticket.py
|    |    |----realname.py
|    |    |----reward.py
|    |    |----safety_log.py
|    |----search/
|    |    |----__init__.py
|    |----user/
|    |    |----relation/
|    |    |    |----follower.py
|    |    |    |----following.py
|    |    |    |----modify.py
|    |    |----__init__.py
|    |----video/
|    |    |----__init__.py
|    |    |----like.py
|----tools/
|    |----b23dumper/
|    |    |----__init__.py
|    |----cookie/
|    |    |----cookieClass.py
|    |    |----load_cookie.py
|    |----headers/
|    |    |----headers.py
|    |----mRequests/
|    |    |----mrequests.py
|    |----safety/
|    |    |----captcha.py
|    |    |----wbi.py
|    |----toolClass/
|    |    |----messageClass.py
|    |----vid/
|    |    |----vid.py
|    |----hmac.py
|    |----response.py
|    |----url.py
|----__init__.py
```

</details>

---

- [biliAPI](https://github.com/JiJiucha/biliAPI)
  - api
    <!--- [dynamic](doc/api/dynamic/dynamic.md)-->
    - [login](doc/api/login/login.md)
    - [message](doc/api/message/message.md)
    - my_info
  - Cookie
  - Message
    - MessageContentText
    - MessageContentImage
    - MessageContentRecall
<!--details>
<summary>项目目录结构</summary>
biliAPI/</br>
|  api/
</details-->
