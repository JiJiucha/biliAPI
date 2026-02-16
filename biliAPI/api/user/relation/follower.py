# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import followers_list,followers_list2
from biliAPI.tools.cookie import cookieClass

def get_followings_list(uid,size=50,page=1,order_type='',cookie=cookieClass.null_cookie):
    return mrequests.get(followings_list,params={'ps':size,'pn':page,'vmid':uid,'order_type':order_type},cookie=cookie)
def get_followings_list2(uid,size=50,page=1,order='desc',cookie=cookieClass.null_cookie):
    return mrequests.get(followings_list2,params={'ps':size,'pn':page,'vmid':uid,'order':order},cookie=cookie)