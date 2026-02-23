# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)
from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_video_view, get_video_detail, get_video_desc, get_video_pagelist
from biliAPI.tools.cookie import cookieClass


def get_info(av = None, bv= None, 
             cookie: cookieClass = cookieClass.null_cookie):
    """
    获取视频基本信息
    
    Args:
        av: AV号
        bv: BV号
        cookie: Cookie对象
    
    Returns:
        BiliResponse: 标准化的响应对象
    """
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    if not av and not bv:
        raise ValueError('Either AV or BV must be provided')
    
    return mrequests.get(
        get_video_view,
        params={'aid': av, 'bvid': bv},
        cookie=cookie
    )


def get_detail(av= None, bv = None, 
               cookie: cookieClass = cookieClass.null_cookie):
    """
    获取视频详细信息
    
    Args:
        av: AV号
        bv: BV号
        cookie: Cookie对象
    
    Returns:
        BiliResponse: 标准化的响应对象
    """
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    if not av and not bv:
        raise ValueError('Either AV or BV must be provided')
    
    return mrequests.get(
        get_video_detail,
        params={'aid': av, 'bvid': bv},
        cookie=cookie,
        withwbi=True
    )


def get_desc(av = None, bv = None, 
             cookie: cookieClass = cookieClass.null_cookie):
    """
    获取视频描述
    
    Args:
        av: AV号
        bv: BV号
        cookie: Cookie对象
    
    Returns:
        BiliResponse: 标准化的响应对象
    """
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    if not av and not bv:
        raise ValueError('Either AV or BV must be provided')
    
    return mrequests.get(
        get_video_desc,
        params={'aid': av, 'bvid': bv},
        cookie=cookie
    )


def get_pages(av = None, bv = None, 
              cookie: cookieClass = cookieClass.null_cookie):
    """
    获取视频分页列表
    
    Args:
        av: AV号
        bv: BV号
        cookie: Cookie对象
    
    Returns:
        BiliResponse: 标准化的响应对象
    """
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    if not av and not bv:
        raise ValueError('Either AV or BV must be provided')
    
    return mrequests.get(
        get_video_pagelist,
        params={'aid': av, 'bvid': bv},
        cookie=cookie
    )
