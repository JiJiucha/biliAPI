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
                  *arg, **kwarg):
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
        *arg, **kwarg):
    return _make_request('GET', url, cookie, header, params, withwbi,*arg, **kwarg)


def post(url, cookie=null_cookie, header=None, params=None, withwbi=False, 
         *arg, **kwarg):
    return _make_request('POST', url, cookie, header, params, withwbi, *arg, **kwarg)

