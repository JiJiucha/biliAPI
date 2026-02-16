# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import is_realname,realname_info

def get_is_realname(cookie):
    return mrequests.get(is_realname,cookie=cookie)

def get_realname_info(cookie):
    return mrequests.get(realname_info,cookie=cookie)