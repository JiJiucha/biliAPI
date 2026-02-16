# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

import json,re,requests

# 解析b23.tv得到bv号
def get_vid(b23):
    if not b23.startswith('https://b23.tv/'):
        return 500,'URL错误'
    # 获取重定向后的URL
    r=requests.get(b23)
    try:
        r.json()['code']==-404
        return 404,r.json()['message']
    except:
        ...
    # 同时支持BV和av号
    # 截取AV或BV
    video_id = re.search(r'(BV[a-zA-Z0-9]{10}|av\d+)', r.url)
    if video_id:
        vid = video_id.group(1)
        if vid.startswith('av'):
            return 'AV',vid
        
        if vid.startswith('BV'):
            return 'BV',vid
        