# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.cookie import cookieClass

import json

def load(fp):
    f=open(fp)
    j=json.load(f)
    return cookieClass.Cookie(j['cookie'],j['refresh_token'])
def save(cookie,fp):
    c={'cookie':cookie.cookie,'refresh_token':cookie.refresh_token}
    f=open(fp,'w')
    j=json.dump(c,f)
    return c