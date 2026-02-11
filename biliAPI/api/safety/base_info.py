from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import my_base_info

def get_base_info(cookie):
    return mrequests.get(my_base_info,cookie=cookie)