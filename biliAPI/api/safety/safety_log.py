# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api
from biliAPI.tools.cookie import cookieClass

def get_coin_log(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.log.coin_log'),cookie=cookie)

def get_exp_log(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.log.exp_log'),cookie=cookie)

def get_moral_log(cookie:cookieClass.Cookie):
    return mrequests.get(api('safety.log.moral_log'),cookie=cookie)