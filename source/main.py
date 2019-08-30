import eel
from json import dumps, load
from os import mkdir, getcwd
from shutil import copy2, rmtree
from file_handler import getFile, expanduser, join, basename
from reader import read_csv

eel.init("UI")

@eel.expose
def getTemplate():
	return getFile("template")

@eel.expose
def getCSV():
	return getFile("csv")

@eel.expose
def startProgram(event_name, template, csv):
	if event_name and template and csv:
		try:
			mkdir("UI/temp")
		except:
			pass

		copy2(template, join("UI/temp", basename(template)))

		with open(join("UI/temp", "dsc-cert-gen.json"), "w") as f:
			f.write(dumps({"event_name": event_name, "template": join("temp", basename(template)), "csv": csv}))
		return True
	else:
		return False

@eel.expose
def setupEditor():
	with open(join("UI/temp", "dsc-cert-gen.json")) as f:
		j = load(f)
	return [j["event_name"], j["template"], read_csv(j["csv"], only_cols=True)]

def cleanup():
	rmtree("UI/temp")

eel.start("index.html")
