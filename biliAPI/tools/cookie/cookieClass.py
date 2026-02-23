# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from urllib import parse
from requests import Response,cookies

class Cookie:
    is_null=False
    cookie=dict()
    def __init__(self,cookie,refresh_token='test_cookie_without_refresh_token'):
        if isinstance(cookie,dict):
            self.cookie=cookie
            self.refresh_token=refresh_token
        else:
            raise TypeError('cookie must be dict,not '+str(cookie.__class__))
    def set(self,key,value):
        self.cookie[key]=value
    
    def get(self,key,default=None):
        return self.cookie.get(key,default)
        
    def delete(self,key):
        if key in self.cookie:
            del self.cookie[key]
    
    def has(self,key):
        return key in self.cookie
        
    def __str__(self):
        return '; '.join([f'{parse.quote(i)}={parse.quote(self.cookie[i])}' for i in self.cookie.keys()])
    def __dict__(self):
        return self.cookie
class _null_cookie(Cookie):
    is_null=True
    def __init__(self):
        self.cookie={}
        self.refresh_token=''
null_cookie=_null_cookie()

def from_requests(arg):
    if isinstance(arg,Response):
        return Cookie(dict(arg.cookies),arg.json()['data']['refresh_token'])
    raise TypeError(f'this type({str(arg.__class__)}) can not dump refresh_token')