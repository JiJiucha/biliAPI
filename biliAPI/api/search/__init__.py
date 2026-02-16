# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import search_all,search_type
from biliAPI.tools.cookie import cookieClass

def kwd_all(keyword,cookie=cookieClass.null_cookie):
    return mrequests.get(search_all,params={'keyword':keyword},cookie=cookie,withwbi=True)
def get_info(uid,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_info,params={'mid':uid},cookie=cookie,withwbi=True)