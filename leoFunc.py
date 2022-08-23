'''
leoFunc.py
By. Nanahira Monke Kanade Dev
'''
import random
import math
import json
import base64

def baseResp(incResp):
    baseResp = base64.standard_b64encode(bytes(incResp, 'utf-8'))
    baseRespShort = baseResp[:1500]
    return baseRespShort

def binResp(incResp):
    binaryResp = ' '.join(format(ord(x), 'b') for x in incResp)
    binaryRespShort = binaryResp[:1500]
    return binaryRespShort

def hexResp(incResp):
    respPrep = incResp.encode('utf-8')
    hexResp = respPrep.hex()
    hexRespShort = hexResp[:1500]
    return hexRespShort
