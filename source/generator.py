from PIL import Image, ImageFont, ImageDraw
from os import mkdir
from os.path import join, exists
from random import randint
from file_handler import read_data
from json import load

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

    data = read_data(j["csv"])

    if options["id_col"] != "none":
        id_col = 0
        for i, k in enumerate(data[1]):
            if k == options["id_col"]:
                id_col = i
                break
    else:
        id_col = None

    raw_img = Image.open(join("UI", j["template"]))
    for d in data[0]:
        img = raw_img.copy()
        draw = ImageDraw.Draw(img)
        for i, _ in enumerate(j["data"]):
            text = str(d[i]).strip()
            font = ImageFont.truetype("UI\assets\socicon\fonts\ARLRDBD.TTF", int(_["font_size"]))

            x, y = float(_["location_x"]), float(_["location_y"])
            w, h = draw.textsize(text, font=font)
            W, H = img.size
            if _["align_center"]:
                x = (W - w) / 2

            draw.text((x, y), text, fill=str(_["font_color"]), font=font)

        if options["extension"] == "none":
            extension = j["template"].split(".")[-1]
        else:
            extension = options["extension"]

        if j["template"].split(".")[-1].lower() == "png":
            if len(img.split()) == 4:
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
                del background

        if id_col != None:
            unique_name = str(d[id_col]).strip().replace(" ", "-")
        else:
            unique_name = str(randint(int(options["id_random_min"]), int(options["id_random_max"])))
        if options["gen_rand"]:
            while True:
                rand_id = randint(int(options["id_random_min"]), int(options["id_random_max"]))
                unique_name += "-" + str(rand_id)
                if not exists(join(j["event_name"], unique_name + "." + extension)):
                    break
        outfilename = join(j["event_name"], unique_name + "." + extension)
        img.save(outfilename)
