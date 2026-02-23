from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import dynamic_get_all_url,dynamic_get_update_url
from biliAPI.tools.cookie import cookieClass


def get_all(cookie,offset=''):
    return mrequests.get(dynamic_get_all_url,params={'offset':offset},cookie=cookie)

def get_update_num(cookie):
    return mrequests.get(dynamic_get_update_url,params={'update_baseline':'0'},cookie=cookie)