# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import login_logout

def logout(cookie):
    return mrequests.post(login_logout,cookie=cookie,data={'biliCSRF':cookie.get('bili_jct')})