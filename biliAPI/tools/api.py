# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

import os
import json

api_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'api-list.json')
)

def api(parts):
    if isinstance(parts,str):
        return api(parts.split('.'))

    if len(parts) < 1:
        raise ValueError('At least one path part is required')
    
    with open(api_path) as f:
        api_dict = json.load(f)
    
    current = api_dict
    for i, part in enumerate(parts):
        # 确保当前层级是字典，否则无法继续查找
        if not isinstance(current, dict):
            raise KeyError(f"Expected a dictionary at path segment '{part}', but got {type(current).__name__}")
        if part not in current:
            raise KeyError(f"Path part '{part}' not found in the current level")
        current = current[part]
    
    # 循环结束后，current 应为 URL 字符串
    if not isinstance(current, str):
        raise KeyError(f"The final value is not a string (URL), got {type(current).__name__}")
    return current