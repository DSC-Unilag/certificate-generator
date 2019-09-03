from os import mkdir
from shutil import copy2, rmtree
from os.path import basename, join
from json import load, dumps
from reader import read_csv
from generator import get_dim

def start(event_name, template, csv):
    try:
        mkdir("UI/temp")
    except:
        pass

    copy2(template, join("UI/temp", basename(template)))
    copy2(csv, join("UI/temp", basename(csv)))

    with open(join("UI/temp", "dsc-cert-gen.json"), "w") as f:
        f.write(dumps({"event_name": event_name, "template": join("temp", basename(template)), "csv": join("UI/temp", basename(csv))}))

def loadEditor():
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)
    j["width"], j["height"] = get_dim(join("UI", j["template"]))
    j["basename"] = basename(j["template"])
    return j

def loadOptions():
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)

    event_name = j["event_name"]
    cols = read_csv(j["csv"], only_cols=True)
    html = ""

    for i, j in enumerate(cols):
        html += '<option value="{}">{}</option>'.format(i, j)
    return [event_name, html]

def cleanup():
	rmtree("UI/temp")
