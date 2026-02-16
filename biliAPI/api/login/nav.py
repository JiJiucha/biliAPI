# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import nav_info
from biliAPI.tools.cookie import cookieClass
#PS:本接口可以不使用cookie
def get_nav_info(cookie=cookieClass.null_cookie):
    return mrequests.get(nav_info,cookie=cookie)