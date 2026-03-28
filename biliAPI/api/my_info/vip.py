# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import vip_info
from biliAPI.tools.cookie import cookieClass

def get_vip_info(cookie:cookieClass.Cookie):
    return mrequests.get(vip_info,cookie=cookie)