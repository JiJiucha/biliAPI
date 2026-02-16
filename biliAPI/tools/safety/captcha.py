# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.cookie import cookieClass

register_url='https://api.bilibili.com/x/gaia-vgate/v1/register'
validate_url='https://api.bilibili.com/x/gaia-vgate/v1/validate'
def register(v_voucher,cookie=cookieClass.null_cookie):
    return mrequests.post(register_url,data={'csrf':cookie.get('bili_jct',''),'v_voucher':v_voucher})
def validate(challenge,token,validate,seccode,cookie=cookieClass.null_cookie):
    return mrequests.post(validate_url,data={'csrf':cookie.get('bili_jct',''),'challenge':challenge,'token':token,'validate':validate,'seccode':seccode},cookie=cookie,withwbi=True)