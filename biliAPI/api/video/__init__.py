# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

"""
视频相关API
使用标准化的响应结构
"""

from typing import Optional, Union
from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_video_view, get_video_detail, get_video_desc, get_video_pagelist
from biliAPI.tools.cookie import cookieClass


def get_info(av: Optional[str] = None, bv: Optional[str] = None, 
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


def get_detail(av: Optional[str] = None, bv: Optional[str] = None, 
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


def get_desc(av: Optional[str] = None, bv: Optional[str] = None, 
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


def get_pages(av: Optional[str] = None, bv: Optional[str] = None, 
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


# 向后兼容的原始响应函数
def get_info_raw(av=None, bv=None, cookie=cookieClass.null_cookie):
    """获取视频基本信息（原始响应，向后兼容）"""
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    return mrequests.get_raw(get_video_view, params={'aid': av, 'bvid': bv}, cookie=cookie)


def get_detail_raw(av=None, bv=None, cookie=cookieClass.null_cookie):
    """获取视频详细信息（原始响应，向后兼容）"""
    if av and bv:
        raise TypeError('Only one of AV and BV can be selected')
    return mrequests.get_raw(get_video_detail, params={'aid': av, 'bvid': bv}, cookie=cookie, withwbi=True)