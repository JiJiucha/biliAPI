from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_user_card,get_user_info
from biliAPI.tools.cookie import cookieClass

def get_card(uid,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_card,params={'mid':uid},cookie=cookie)
def get_info(uid,cookie=cookieClass.null_cookie):
    return mrequests.get(get_user_info,params={'mid':uid},cookie=cookie,withwbi=True)