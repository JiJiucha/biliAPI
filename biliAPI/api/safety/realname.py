# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api
from biliAPI.tools.cookie import cookieClass

def get_is_realname(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.realname.is_realname'),cookie=cookie)

def get_realname_info(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.realname.realname_info'),cookie=cookie)