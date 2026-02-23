# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_buvid3_url,get_buvid_url

def get_buvid3():
    return mrequests.get(get_buvid3_url)
def get_buvid():
    return mrequests.get(get_buvid_url)