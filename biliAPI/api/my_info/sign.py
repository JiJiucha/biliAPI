from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import update_sign

def update(cookie,sign):
    return mrequests.post(update_sign,cookie=cookie,data={'user_sign':sign,'csrf':cookie.get('bili_jct')})

def clean(cookie):
    return update(cookie=cookie,sign='')