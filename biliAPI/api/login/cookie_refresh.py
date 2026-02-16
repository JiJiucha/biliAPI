# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.makeurl import makeurl
from biliAPI.tools.url import is_cookie_need_refresh,get_refresh_csrf_web,refresh_cookie,confirm_refresh

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


def is_need_refresh(cookie):
    return mrequests.get(is_cookie_need_refresh,cookie=cookie)



def get_refresh_csrf(cookie):
    ts = round(time.time() * 1000)
    correspondPath=getCorrespondPath(ts)
    r=mrequests.get(makeurl(get_refresh_csrf_web,correspondPath),cookie=cookie,params={'csrf':cookie.get('bili_jct')})[1]
    
    js=r.json()
    
    soup = BeautifulSoup(json, 'html.parser')
    
    refresh_csrf=soup.find('div',id='1-name')
    
    return refresh_csrf
    
def refresh_cookie(cookie,refreshv_csrf,refresh_token):
    return mrequests.post(refresh_cookie,cookie=cookie,params={'csrf':cookie.get('bili_jct'),'refresh_csrf':refresh_csrf,'source':'main_web','refresh_token':refresh_token})
    

def confirm_refresh_cookie(cookie,refresh_token):#PS:新cookie，旧refresh_token
    return mrequests.post(confirm_refresh,cookie=cookie,params={'csrf':cookie.get('bili_jct'),'refresh_token':refresh_token})