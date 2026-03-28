# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

"""
biliAPI统一响应类
提供标准化的API返回结构，包含数据、状态码、消息和原始响应
"""
import json
from typing import Any, Dict, Optional, Union
from dataclasses import dataclass

from biliAPI.tools import json_objects

@dataclass
class BiliResponse:
    """B站API统一响应类"""
    
    # 核心数据字段
    data: Any = None
    code: int = 0
    message: str = ""
    
    # 原始响应信息
    success: bool = False
    raw_response: Optional[Any] = None
    http_status: int = 0
    headers: Dict[str, str] = None
    
    has_more=False
    
    def __post_init__(self):
        """初始化后处理"""
        if self.headers is None:
            self.headers = {}
    
    @property
    def is_success(self) -> bool:
        """检查请求是否成功（HTTP状态码和B站API状态码都成功）"""
        return self.success and self.code == 0
    
    #@property
    def json(self):
        return json_objects.loads(self.raw_response.text)
    def raise_for_status(self):
        return self.raw_response.raise_for_status()
        
    @property
    def text(self):
        return self.raw_response.text
    
    @property
    def has_data(self) -> bool:
        """检查是否有数据"""
        return self.data is not None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'success': self.success,
            'code': self.code,
            'message': self.message,
            'data': self.data,
            'http_status': self.http_status
        }
    
    def __str__(self) -> str:
        """字符串表示"""
        status = "✓" if self.is_success else "✗"
        return f"BiliResponse[{status}] code={self.code}, message='{self.message}', data={type(self.data).__name__}"


class ResponseBuilder:
    """响应构建器"""
    
    @staticmethod
    def from_mrequests_result(result: tuple, parse_json: bool = True) -> BiliResponse:
        success, response, text = result
        
        # 创建基础响应
        bili_response = BiliResponse(
            success=success,
            http_status=response.status_code if response else 0,
            headers=dict(response.headers) if response else {}
        )
        
        # 如果没有文本内容
        if not text:
            bili_response.message = "No response content"
            return bili_response
        
        # 尝试解析JSON
        if parse_json:
            try:
                import json
                json_data = json.loads(text)
                
                # 提取B站API的标准字段
                bili_response.code = json_data.get('code', -1)
                bili_response.message = json_data.get('message', '')
                bili_response.data = json_objects.from_python(json_data.get('data'))
                
            except json.JSONDecodeError:
                # 如果不是JSON，将原始文本作为数据
                bili_response.data = text
                bili_response.message = "Response is not JSON"
        else:
            # 不解析JSON，直接使用文本
            bili_response.data = text
        
        # 保存原始响应
        bili_response.raw_response = response
        
        return bili_response
    
    @staticmethod
    def success(data: Any = None, message: str = "Success", **kwargs) -> BiliResponse:
        """创建成功响应"""
        return BiliResponse(
            success=True,
            code=0,
            message=message,
            data=data,
            http_status=200,
            **kwargs
        )
    
    @staticmethod
    def error(code: int, message: str, http_status: int = 400, **kwargs) -> BiliResponse:
        """创建错误响应"""
        return BiliResponse(
            success=False,
            code=code,
            message=message,
            http_status=http_status,
            **kwargs
        )
    
    @staticmethod
    def http_error(http_status: int, message: str = None) -> BiliResponse:
        """创建HTTP错误响应"""
        if message is None:
            from http.client import responses
            message = responses.get(http_status, f"HTTP {http_status}")
        
        return BiliResponse(
            success=False,
            code=http_status,
            message=message,
            http_status=http_status
        )


# 快捷函数
def make_response(result: tuple, parse_json: bool = True) -> BiliResponse:
    """从mrequests结果创建响应（快捷函数）"""
    return ResponseBuilder.from_mrequests_result(result, parse_json)