#! /usr/bin/python3
# coding: utf-8
import os, datetime, secrets, string
import qrcode
from PIL import Image, ImageDraw, ImageFont
import requests, json

# Please Write Your Wi-Fi Setting & Slack Token & Font Path
CONPANY_NAME        = 'GUEST'
ENCRYPTION_METHOD   = 'WPA'
SLACK_TOKEN         = ''
SLACK_CHANNEL       = 'freewifi-dev'
FONT_PATH           = '/usr/share/fonts/dejavu/DejaVuSans.ttf'

# Password Length & Font Size Setting
PASSWORD_MAX_LENGTH = 16
FONT_SIZE           = 20

# PIL Size property index
WIDTH_INDEX         = 0
HEIGHT_INDEX        = 1

# Base Image Height
BASE_IMAGE_HEIGHT   = 60
#########################################################
## main
#########################################################
## Example
## SSID:GUEST-2020-01
## Password:XAjSgVPrWlS6AJRX
#########################################################

# Create SSID & Password & Qrcode
carete_timestamp                = datetime.datetime.now()
monthly_ssid                    = CONPANY_NAME + '{0:-%Y-%m}'.format(carete_timestamp)
monthly_password                = ''.join([secrets.choice(string.ascii_letters) for i in range(PASSWORD_MAX_LENGTH) ])
wifi_conneting_infomation       = 'WIFI:T:' + ENCRYPTION_METHOD + ';S:' + monthly_ssid + ';P:' + monthly_password + ';;'
wifi_conneting_infomation_list  = ['SSID: ' + monthly_ssid , 'Password: ' + monthly_password]

# Create QR Code Image
qrcode_image                    = qrcode.make(wifi_conneting_infomation)

# Create Wi-Fi Infomation Image
base_image                      = Image.new('RGB', (qrcode_image.size[WIDTH_INDEX], BASE_IMAGE_HEIGHT), 'white')
wifi_conneting_infomation_draw  = ImageDraw.Draw(base_image)
wifi_conneting_infomation_font  = ImageFont.truetype(FONT_PATH,FONT_SIZE)
writing_position = 0
for printing_inromation in wifi_conneting_infomation_list:
    wifi_conneting_infomation_draw.multiline_text((0,
                                                   writing_position),
                                                   printing_inromation,
                                                   fill=(0, 0, 0),
                                                   font=wifi_conneting_infomation_font)
    writing_position = writing_position + FONT_SIZE

# Concat QR code Image & Wi-Fi Infomation Image
wifi_conneting_infomation_image = Image.new('RGB',
                                            (qrcode_image.size[WIDTH_INDEX],
                                             qrcode_image.size[HEIGHT_INDEX] + base_image.size[HEIGHT_INDEX]))

wifi_conneting_infomation_image.paste(qrcode_image,(0,0))
wifi_conneting_infomation_image.paste(base_image,(0,qrcode_image.size[HEIGHT_INDEX]))

# Saving wifi_conneting_infomation_image
wifi_conneting_infomation_image_path = os.curdir + '/' + '{0:%Y%m%d-%H%M%S}'.format(carete_timestamp) +'result.png'
wifi_conneting_infomation_image.save(wifi_conneting_infomation_image_path)

# Throw wifi_conneting_infomation_image to Slack
param = {'token':SLACK_TOKEN, 'channels':SLACK_CHANNEL,'initial_comment': '/'.join(wifi_conneting_infomation_list)}
files = {'file': open(wifi_conneting_infomation_image_path, 'rb')}
requests.post(url='https://slack.com/api/files.upload',params=param, files=files)
