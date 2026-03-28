# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api

def logout(cookie:cookieClass.Cookie):
    return mrequests.post(api('login.login.web.logout'),cookie=cookie,data={'biliCSRF':cookie.get('bili_jct')})