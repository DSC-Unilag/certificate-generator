from os import mkdir
from shutil import copy2, rmtree
from os.path import basename, join
from json import load, dumps
from file_handler import read_data
from generator import get_dim

def start(event_name, template, csv):
    try:
        mkdir("UI/temp")
    except:
        pass

    for x in [(template, basename(template)), (csv, basename(csv))]:
        try:
            copy2(x[0], join("UI/temp", x[1]))
        except:
            pass

    with open(join("UI/temp", "dsc-cert-gen.json"), "w") as f:
        f.write(dumps({"event_name": event_name, "template": join("temp", basename(template)), "csv": join("UI/temp", basename(csv))}))

def saveEditor(trans):
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)

    j["data"] = trans

    with open(join("UI/temp", "dsc-cert-gen.json"), "w") as f:
        f.write(dumps(j))

def loadEditor():
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)
    j["width"], j["height"] = get_dim(join("UI", j["template"]))
    j["template_base"] = basename(j["template"])
    j["csv_base"] = basename(j["csv"])
    return j

def loadOptions():
    with open(join("UI/temp", "dsc-cert-gen.json")) as f:
        j = load(f)

    event_name = j["event_name"]
    cols = read_data(j["csv"], only_cols=True)
    html = ""

    for i, j in enumerate(cols):
        html += '<option value="{}">{}</option>'.format(i, j)
    return [event_name, html]

def cleanup():
	rmtree("UI/temp")
