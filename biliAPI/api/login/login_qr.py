# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import generate_web_url,poll_web_url

class login_qr_code:
    success=0
    invalid=86038
    scan_but_no_confirm=86090
    unscan=86101

def generate_web():
    return mrequests.get(generate_web_url)
def poll_web(key):
    return mrequests.get(poll_web_url,params={'qrcode_key':key})
