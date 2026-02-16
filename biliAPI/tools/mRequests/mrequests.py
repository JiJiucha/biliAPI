# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

"""
增强版mRequests模块
支持标准化的响应结构和更好的错误处理
"""

import requests
from typing import Optional, Dict, Any, Tuple
from biliAPI.tools.headers import headers as global_headers
from biliAPI.tools.cookie.cookieClass import Cookie, null_cookie
from biliAPI.tools.safety import wbi
from biliAPI.tools.response import BiliResponse, ResponseBuilder, make_response


def wbi_sign(params):
    """WBI签名"""
    img, sub = wbi.getWbi()
    signed_params = wbi.encWbi(params=params, img_key=img, sub_key=sub)
    return signed_params


def _prepare_params(params, cookie, withwbi):
    """准备请求参数"""
    # 过滤空值参数
    processed_params = {k: v for k, v in (params or {}).items() if v}
    
    # 添加gaia_vtoken
    if cookie.get('x-bili-gaia-vtoken'):
        processed_params['gaia_vtoken'] = cookie.get('x-bili-gaia-vtoken')
    
    # WBI签名
    if withwbi:
        processed_params = wbi_sign(processed_params)
    
    return processed_params


def _prepare_headers(custom_headers):
    """准备请求头，不污染全局headers"""
    # 创建新的headers字典，合并全局headers和自定义headers
    return {**global_headers.headers, **custom_headers}


def _make_request(method, url, cookie=null_cookie, header=None, params=None, withwbi=False, 
                  return_raw: bool = False, *arg, **kwarg):
    """
    通用请求函数
    
    Args:
        method: HTTP方法
        url: 请求URL
        cookie: Cookie对象
        header: 自定义请求头
        params: 请求参数
        withwbi: 是否使用WBI签名
        return_raw: 是否返回原始三元组（兼容旧代码）
        *arg, **kwarg: 其他requests参数
    
    Returns:
        如果return_raw为True，返回原始三元组 (success, response, text)
        否则返回BiliResponse对象
    """
    # 准备请求头（使用空字典作为默认值）
    request_headers = _prepare_headers(header or {})
    
    # 准备参数
    processed_params = _prepare_params(params, cookie, withwbi)
    
    try:
        # 发送请求
        response = requests.request(
            method, 
            url, 
            headers=request_headers, 
            cookies=cookie.cookie, 
            params=processed_params, 
            *arg, 
            **kwarg
        )
        
        # 返回结果
        success = response.ok
        text = response.text if success else None
        
        # 根据return_raw参数决定返回格式
        if return_raw:
            return success, response, text
        
        # 返回标准化的响应对象
        return ResponseBuilder.from_mrequests_result((success, response, text))
        
    except requests.RequestException as e:
        # 处理请求异常
        if return_raw:
            return False, None, None
        
        # 返回错误响应
        return ResponseBuilder.error(
            code=-1,
            message=f"Request failed: {str(e)}",
            http_status=0
        )


def get(url, cookie=null_cookie, header=None, params=None, withwbi=False, 
        return_raw: bool = False, *arg, **kwarg):
    """
    GET请求
    
    Args:
        return_raw: 是否返回原始三元组（兼容旧代码）
    
    Returns:
        如果return_raw为True，返回原始三元组
        否则返回BiliResponse对象
    """
    return _make_request('GET', url, cookie, header, params, withwbi, return_raw, *arg, **kwarg)


def post(url, cookie=null_cookie, header=None, params=None, withwbi=False, 
         return_raw: bool = False, *arg, **kwarg):
    """
    POST请求
    
    Args:
        return_raw: 是否返回原始三元组（兼容旧代码）
    
    Returns:
        如果return_raw为True，返回原始三元组
        否则返回BiliResponse对象
    """
    return _make_request('POST', url, cookie, header, params, withwbi, return_raw, *arg, **kwarg)


# 向后兼容的快捷函数
def get_raw(*args, **kwargs):
    """获取原始响应（向后兼容）"""
    return get(*args, **kwargs, return_raw=True)


def post_raw(*args, **kwargs):
    """获取原始响应（向后兼容）"""
    return post(*args, **kwargs, return_raw=True)