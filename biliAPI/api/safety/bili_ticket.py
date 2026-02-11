from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import bili_ticket_get

import time
#改自BAC
def get_ticket():
    o = hmac_sha256("XgwSnGZ1p",f"ts{int(time.time())}")
    return mrequests.post(bili_ticket_get,header={'Referer':''},params={'key_id':'ec02',"hexsign":o,"context[ts]":f"{int(time.time())}","csrf": ''})