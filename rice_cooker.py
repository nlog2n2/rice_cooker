#! /usr/bin/python3
# coding: utf-8
import secrets 
import string
import qrcode
import PIL
import requests
import datetime
import os

CONPANY_NAME        = 'GUEST'
ENCRYPTION_METHOD   = "WPA"
SLACK_TOKEN         = ''
FONT_PATH           = ''
SSID_MAX_LENGTH     = 12
PASSWORD_MAX_LENGTH = 16

# Example
# SSID:GUEST-2020-01
# Password:XAjSgVPrWlS6AJRX

# Create SSID & Password & Qrcode
monthly_ssid                    = CONPANY_NAME + "{0:-%Y-%m}".format(datetime.datetime.now())
monthly_password                = "".join([secrets.choice(string.ascii_letters) for i in range(PASSWORD_MAX_LENGTH) ])
wifi_conneting_infomation       = "WIFI:T:" + ENCRYPTION_METHOD + ";S:" + monthly_ssid + ";P:" + monthly_password + ";;"
qrcode_image                    = qrcode.make(wifi_conneting_infomation)
# ssid_password_image             = 
# Saving QR Code Image
IS_EXIST_QRCODE_DIR = False
qrcode_image.save('/home/vagrant/rice_cooker/qrcode.png')

# print("SSID: " + monthly_ssid)
# print("Password: " + monthly_password)
# print(wifi_conneting_infomation)

