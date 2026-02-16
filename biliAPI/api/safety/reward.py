# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import day_reward,day_coin_reward

def get_reward(cookie):
    return mrequests.get(day_reward,cookie=cookie)

def get_reward_coin(cookie):
    return mrequests.get(day_coin_reward,cookie=cookie)