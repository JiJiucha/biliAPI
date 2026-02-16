# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import vip_info

def get_vip_info(cookie):
    return mrequests.get(vip_info,cookie=cookie)