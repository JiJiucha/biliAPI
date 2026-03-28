# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api
from biliAPI.tools.cookie import cookieClass

def get_base_info(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.base_info'),cookie=cookie)