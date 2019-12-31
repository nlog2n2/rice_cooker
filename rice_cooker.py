#! /usr/bin/python3
# coding: utf-8
import os, datetime, secrets, string
import qrcode
from PIL import Image, ImageDraw, ImageFont
import requests

CONPANY_NAME        = 'GUEST'
ENCRYPTION_METHOD   = 'WPA'
SLACK_TOKEN         = ''
IMAGE_DIR           = os.path.curdir +'/image'
SSID_MAX_LENGTH     = 20
PASSWORD_MAX_LENGTH = 16

FONT_PATH           = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
FONT_SIZE           = 12
BASE_IMAGE_WIDTH    = 20
BASE_IMAGE_HEIGTH   = 20


#########################################################
## main
#########################################################
## Example
## SSID:GUEST-2020-01
## Password:XAjSgVPrWlS6AJRX
#########################################################

# Create SSID & Password & Qrcode
monthly_ssid                    = CONPANY_NAME + '{0:-%Y-%m}'.format(datetime.datetime.now())
monthly_password                = ''.join([secrets.choice(string.ascii_letters) for i in range(PASSWORD_MAX_LENGTH) ])
wifi_conneting_infomation       = 'WIFI:T:' + ENCRYPTION_METHOD + ';S:' + monthly_ssid + ';P:' + monthly_password + ';;'

qrcode_image                    = qrcode.make(wifi_conneting_infomation)

# Saving QR Code Image
#QRCODE_SAVING_DIR   = os.path
qrcode_image.save('/home/vagrant/rice_cooker/qrcode.png')


# ase_image = create_base_image('RGB', BASE_IMAGE_WIDTH, BASE_IMAGE_HEIGTH, 'white')
# draw = ImageDraw.Draw(base_image)
# font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
# draw.multiline_text((0, 0), 'Pillow sample /n hoge', fill=(0, 0, 0), font=font)

def create_base_image(mode, width, height, color, infomation):
    
    if(os.path.exists(IMAGE_DIR)):
        os.makedirs(IMAGE_DIR)
    
    #BASE_IMAGE_PATH     = IMAGE_DIR + 'base.png' # todo date write
        
    return 0
#Image.new('RGB', (width, height), 'white')

print('SSID: ' + monthly_ssid)
print('Password: ' + monthly_password)
# print(wifi_conneting_infomation)
