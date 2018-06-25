#!/usr/bin/env python
#coding:utf8
import base64
from Crypto.Cipher import AES
from Crypto import Random
import time
 
password = 'southtvsouthtvcc' #16位长的密码
iv = 'abcdefghabcdefgh'

def encrypt(data, password):
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(data)
    return data
 
def decrypt(data, password):
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = cipher.decrypt(data)
    return data

pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def Encrypt(): 
    data = str(int(time.time()))
    encrypt_data = encrypt(pad(data), password)
    encrypt_data = base64.b64encode(encrypt_data)
    return encrypt_data

def Decrypt(encrypt_data): 
    encrypt_data = base64.b64decode(encrypt_data)
    decrypt_data = decrypt(encrypt_data, password)
    return decrypt_data

if __name__ == '__main__':
    encrypt_data = Encrypt()
    print 'encrypt_data:', encrypt_data
 
    decrypt_data = Decrypt(encrypt_data)
    print 'decrypt_data:', decrypt_data 

 
