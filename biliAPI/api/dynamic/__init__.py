# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import dynamic_get_all_url,dynamic_get_update_url
from biliAPI.tools.cookie import cookieClass


def get_all(cookie:cookieClass.Cookie,offset=''):
    return mrequests.get(dynamic_get_all_url,params={'offset':offset},cookie=cookie)

def get_update_num(cookie:cookieClass.Cookie):
    return mrequests.get(dynamic_get_update_url,params={'update_baseline':'0'},cookie=cookie)