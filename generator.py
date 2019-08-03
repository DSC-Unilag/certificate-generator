# This file handles the Certificate Generation
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

def generator(template, data, locations, font=None, font_size=None, font_color=(0, 0, 0)):
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
    outfilename = "certificates/" + "-".join(name.split()) + "-certificate." + template.split(".")[-1]
    img.save(outfilename)
