# This file handles the Certificate Generation
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from random import randint as rand

def sendmail(email, img, login, subject, s):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = email
    msg['Subject'] = subject
    message = "<img src='{}'>".format(img)
    print(message)
    message = "<h1>Hello World</h1>"
    msg.attach(MIMEText(message, 'html', "utf-8"))
    s.send_message(msg)

def generator(template, data, locations, email, font=None, font_size=None, font_color=(225, 174, 46, 255)):
    # font
    font = ImageFont.truetype("ARLRDBD.ttf", 70)

    # open the template file
    img = Image.open(template)
    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])
    img = background
    draw = ImageDraw.Draw(img)

    a = True
    for i in range(len(data)):
        if a:
            font = ImageFont.truetype("ARLRDBD.ttf", 70)
        else:
            font = ImageFont.truetype("ARLRDBD.ttf", 30)
        w, h = draw.textsize(data[i], font=font)
        W, H = img.size
        ww = (W - w) / 2
        draw.text((ww, locations[i][1]), data[i], fill=(225, 174, 46), font=font)
        a = False

    # Check if output destination exists
    if not os.path.exists("certificates/"):
        os.system("mkdir certificates")

    name = data[0]
    outfilename = "certificates/" + name + "-certificate-" + str(rand(1, 476487)) + ".pdf"
    img.save(outfilename)
