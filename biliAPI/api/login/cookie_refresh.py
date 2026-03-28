# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.api import api
from biliAPI.tools.cookie import cookieClass

from bs4 import BeautifulSoup
import json

#----来自BAC
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii
import time

key = RSA.importKey('''\
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLgd2OAkcGVtoE3ThUREbio0Eg
Uc/prcajMKXvkCKFCWhJYJcLkcM2DKKcSeFpD/j6Boy538YXnR6VhcuUJOhH2x71
nzPjfdTcqMz7djHum0qSZA0AyCBDABUqCrfNgCiJ00Ra7GmRj+YCK1NJEuewlb40
JNrRuoEUXpabUzGB8QIDAQAB
-----END PUBLIC KEY-----''')

def getCorrespondPath(ts):
    cipher = PKCS1_OAEP.new(key, SHA256)
    encrypted = cipher.encrypt(f'refresh_{ts}'.encode())
    return binascii.b2a_hex(encrypted).decode()



#----


def is_need_refresh(cookie:cookieClass.Cookie):
    return mrequests.get(api('login.login.cookie_refresh.need_refresh'),cookie=cookie)



def get_csrf(cookie:cookieClass.Cookie):
    ts = round(time.time() * 1000)
    correspondPath = getCorrespondPath(ts)
    # 拼接 URL
    url = api('login.login.cookie_refresh.get_csrf') + correspondPath
    r = mrequests.get(url, cookie=cookie, params={'csrf': cookie.get('bili_jct')})
    soup = BeautifulSoup(r.text, 'html.parser')   # 此处原变量名与模块冲突，建议改为 soup = BeautifulSoup(r.text, 'html.parser')
    refresh_csrf = soup.find('div', id='1-name')
    return refresh_csrf
    
def refresh(cookie:cookieClass.Cookie,refreshv_csrf,refresh_token):
    return mrequests.post(api('login.login.cookie_refresh.refresh'),cookie=cookie,params={'csrf':cookie.get('bili_jct'),'refresh_csrf':refresh_csrf,'source':'main_web','refresh_token':refresh_token})
    

def confirm(cookie:cookieClass.Cookie,refresh_token):
    '''PS:新cookie，旧refresh_token'''
    return mrequests.post(api('login.login.cookie_refresh.confirm'),cookie=cookie,params={'csrf':cookie.get('bili_jct'),'refresh_token':refresh_token})