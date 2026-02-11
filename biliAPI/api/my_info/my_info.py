from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import stat_of_login_user,get_coin_count
from biliAPI.tools.cookie import cookieClass

def get_coin_count(cookie):
    return mrequests.get(get_coin_count,cookie=cookie)

def get_stat_login(cookie):
    return mrequests.get(stat_of_login_user,cookie=cookie)