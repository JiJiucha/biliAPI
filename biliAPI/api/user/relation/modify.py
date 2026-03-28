# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import modify_relation
from biliAPI.tools.cookie import cookieClass


'''
act:
1 关注
2 取关
3 悄悄关注
4 取消悄悄关注
5 拉黑
6 取消拉黑
7 删除粉丝
'''
def _modify(uid,act,cookie:cookieClass.Cookie=cookieClass.null_cookie,re_src=11):
    return mrequests.post(modify_relation,params={'fid':uid,'act':act,'re_src':re_src,'csrf':cookie.get('bili_jct')},cookie=cookie)
def follow(uid,re_src=11,cookie:cookieClass.Cookie):
    return _modify(uid,1,cookie)
def unfollow(uid,cookie:cookieClass.Cookie):
    return _modify(uid,2,cookie)

