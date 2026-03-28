# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import update_sign
from biliAPI.tools.cookie import cookieClass

def update(sign,cookie:cookieClass.Cookie):
    return mrequests.post(update_sign,cookie=cookie,data={'user_sign':sign,'csrf':cookie.get('bili_jct')})

def clean(cookie:cookieClass.Cookie):
    return update(cookie=cookie,sign='')