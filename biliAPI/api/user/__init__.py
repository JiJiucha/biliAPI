# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_user_cards,get_user_card,get_user_info,my_info
from biliAPI.tools.cookie import cookieClass

def get_cards(uids,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_cards,params={'uids':','.join([str(i) for i in uids])},cookie=cookie)
def get_card(uid,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_card,params={'mid':uid},cookie=cookie)
def get_info(uid,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_info,params={'mid':uid},cookie=cookie,withwbi=True)
    
def get_my_info(cookie=cookieClass.null_cookie):
    return mrequests.get(my_info,cookie=cookie)