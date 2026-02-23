# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_notice_unread,get_replies_url

def get_unread_notices(cookie):
    return mrequests.get(get_notice_unread,cookie=cookie)
    
def get_replies(cookie,id_=None):
    return mrequests.get(get_replies_url,cookie=cookie,params={'id':id_})
    