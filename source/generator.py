from PIL import Image, ImageFont, ImageDraw
from os import mkdir
from os.path import join
from random import randint

def get_dim(path):
    img = Image.open(path)
    return img.width, img.height

def gen_img(options):
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)
    try:
        mkdir(j["event_name"])
    except:
        pass

    for data in img_data:
        img = Image.open(join("UI", j["template"]))
        draw = ImageDraw.Draw(img)
        index = 0
        for point in img_points:
            font = ImageFont.truetype(point["font_name"], point["font_size"])
            x, y = point["x"], point["y"]
            w, h = draw.textsize(data[index], font=font)
            W, H = img.size
            if center_width:
                x = (W - w) / 2
            if center_height:
                y = (H - h) / 2
            draw.text((x, y), data[index], fill=point["font_color"], font=font)
            index += 1

        if extension == None:
            extension = j["template"].split(".")[-1]

        if extension.lower() == "png":
            if len(img.split()) == 4:
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
                del background

        if allow_random:
            unique_name = data[id_] + "-" + str(rand(1, 10000))
        else:
            unique_name = data[id_]

        outfilename = join(j["event_name"], unique_name + "." + extension)
        img.save(outfilename)
