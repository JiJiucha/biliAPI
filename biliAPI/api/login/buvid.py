# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api

def get_buvid3():
    return mrequests.get(api('login.login.buvid.buvid3'))
def get_buvid():
    return mrequests.get(api('login.login.buvid.buvid'))