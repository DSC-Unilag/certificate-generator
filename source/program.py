from os import mkdir
from shutil import copy2, rmtree
from os.path import basename, join
from json import load, dumps
from generator import get_dim

def start(event_name, template, csv):
    try:
        mkdir("UI/temp")
    except:
        pass

    copy2(template, join("UI/temp", basename(template)))

    with open(join("UI/temp", "dsc-cert-gen.json"), "w") as f:
        f.write(dumps({"event_name": event_name, "template": join("temp", basename(template)), "csv": csv}))

def loadEditor():
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)
    j["width"], j["height"] = get_dim(join("UI", j["template"]))
    return j

def cleanup():
	rmtree("UI/temp")
