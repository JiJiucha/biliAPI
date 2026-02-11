from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import my_account_info

def get_account_info(cookie):
    return mrequests.get(my_account_info,cookie=cookie)