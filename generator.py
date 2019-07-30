# This file handles the Certificate Generation
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

def generator(name, template, program_name, certification_date):
    # open the template file
    img = Image.open(template)
    draw = ImageDraw.Draw(img)
    draw.text((298, 314), name, (0, 0, 0))
    draw.text((226, 423), program_name, (0, 0, 0))
    draw.text((435, 627), certification_date, (0, 0, 0))

    # Check if output destination exists
    if not os.path.exists("certificates/"):
        os.system("md certificates")

    outfilename = "certificates/" + "-".join(name.split()) + "-certificate." + template.split(".")[-1]
    img.save(outfilename)

generator("Solomon Ghost", "img/certificate-sample.jpeg", "PYTHON CLASS", "JULY 2019")
