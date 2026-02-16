# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import coin_log,exp_log,moral_log

def get_coin_log(cookie):
    return mrequests.get(coin_log,cookie=cookie)

def get_exp_log(cookie):
    return mrequests.get(day_coin_reward,cookie=cookie)

def get_moral_log(cookie):
    return mrequests.get(moral_log,cookie=cookie)