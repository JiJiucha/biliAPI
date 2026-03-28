# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_notice_unread,get_replies_url
from biliAPI.tools.cookie import cookieClass

def get_unread_notices(cookie:cookieClass.Cookie):
    return mrequests.get(get_notice_unread,cookie=cookie)
    
def get_replies(cookie:cookieClass.Cookie,id_=None):
    return mrequests.get(get_replies_url,cookie=cookie,params={'id':id_})
    