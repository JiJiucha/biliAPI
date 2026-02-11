from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import followings_list,followings_list2,search_following_list,same_followings_list
from biliAPI.tools.cookie import cookieClass

def get_followings_list(uid,size=50,page=1,order_type='',cookie=cookieClass.null_cookie):
    return mrequests.get(followings_list,params={'ps':size,'pn':page,'vmid':uid,'order_type':order_type},cookie=cookie)
def get_followings_list2(uid,size=50,page=1,order='desc',cookie=cookieClass.null_cookie):
    return mrequests.get(followings_list2,params={'ps':size,'pn':page,'vmid':uid,'order':order},cookie=cookie)
    
def search_followings(uid,size=50,page=1,name=None,cookie=cookieClass.null_cookie):
    return mrequests.get(search_following_list,params={'ps':size,'pn':page,'vmid':uid,'name':name},cookie=cookie)

def same_followings(uid,size=50,page=1,cookie=cookieClass.null_cookie):
    return mrequests.get(same_followings_list,params={'ps':size,'pn':page,'vmid':uid},cookie=cookie)
    
    