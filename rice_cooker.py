#! /usr/bin/python3
# coding: utf-8
import secrets 
import string
import qrcode, PIL
import requests
import datetime

CONPANY_NAME        = 'GUEST'
ENCRYPTION_METHOD   = "WPA"
SLACK_TOKEN         = ''
SSID_MAX_LENGTH     = 12
PASSWORD_MAX_LENGTH = 16

# Example
# SSID:GUEST-2020-01
# Password:XAjSgVPrWlS6AJRX

# Create SSID & Password
ssid        = CONPANY_NAME + "{0:-%Y-%m}".format(datetime.datetime.now())
password    = "".join([secrets.choice(string.ascii_letters) for i in range(PASSWORD_MAX_LENGTH) ])

# print("SSID: " + ssid)
# print("Password: " + password)

# Create QR code Image 
qrcode      = "WIFI:" + ENCRYPTION_METHOD + ";S:" + ssid + ";P:" + password + ";;"

print(qrcode)
# Create printed SSID & Password Image 
# Pasted Image



