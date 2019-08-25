# This file handles the Certificate Generation
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendmail(email, img, login, subject, s):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = email
    msg['Subject'] = subject
    message = "<img src='{}'>".format(img)
    print(message)
    input()
    msg.attach(MIMEText(message, 'html', "utf-8"))
    s.send_message(msg)

def generator(template, data, locations, email, font=None, font_size=None, font_color=(0, 0, 0)):
    # font
    font = ImageFont.truetype("Eutemia.ttf", 44)

    # open the template file
    img = Image.open(template)
    draw = ImageDraw.Draw(img)

    for i in range(len(data)):
        draw.text((locations[i][0], locations[i][1]), data[i], font_color, font=font)

    # Check if output destination exists
    if not os.path.exists("certificates/"):
        os.system("mkdir certificates")

    name = data[0]
    outfilename = "certificate." + template.split(".")[-1]
    img.save(outfilename)
    with open(outfilename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    host, port = "wtpccorp.com", "2096"
    login, password = "support@wtpccorp.com", "okey1493"
    subject = "Here is your certificate"
    s = smtplib.SMTP_SSL(host=host, port=port)
    s.starttls()
    s.login(login, password)
    sendmail(email, encoded_string, login, subject, s)
