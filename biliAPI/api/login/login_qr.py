# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api


class login_qr_code:
    success=0
    invalid=86038
    scan_but_no_confirm=86090
    unscan=86101

def generate_web():
    return mrequests.get(api('login.login.web.qr.generate'))
def poll_web(key):
    return mrequests.get(api('login.login.web.qr.poll'),params={'qrcode_key':key})
