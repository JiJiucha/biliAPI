# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import like_video_url
from biliAPI.tools.cookie import cookieClass


def _like(cookie,like,av=None,bv=None):
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    if not av and not bv:
        raise ValueError('Either AV or BV must be provided')
    return mrequests.post(like_video_url,params={'aid':av,'bvid':bv,'like':like,'csrf':cookie.get('bili_jct')},cookie=cookie)