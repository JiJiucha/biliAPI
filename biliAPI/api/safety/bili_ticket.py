# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api


import time
#改自BAC
def get_ticket():
    o = hmac_sha256("XgwSnGZ1p",f"ts{int(time.time())}")
    return mrequests.post(api('safety.bili_ticket'),header={'Referer':''},params={'key_id':'ec02',"hexsign":o,"context[ts]":f"{int(time.time())}","csrf": ''})