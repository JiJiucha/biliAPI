from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import login_qr_web_generate,login_qr_web_poll

class login_qr_code:
    success=0
    invalid=86038
    scan_but_no_confirm=86090
    unscan=86101

def generate_web():
    return mrequests.get(login_qr_web_generate)
def poll_web(key):
    return mrequests.get(login_qr_web_poll,params={'qrcode_key':key})
