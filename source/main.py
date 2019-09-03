import eel
from file_handler import getFile
from json import load
from os.path import join
from program import start, loadEditor, cleanup, loadOptions
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
		start(event_name, template, csv)
		return True
	else:
		return "incomplete"

@eel.expose
def setupEditor():
	j = loadEditor()
	return [j["event_name"], [j["template"], j["width"], j["height"]], read_csv(j["csv"], only_cols=True), j["template_base"], j["csv_base"]]

@eel.expose
def setupOptions():
	opts = loadOptions()
	return opts

@eel.expose
def finish():
	with open(join("UI/temp", "dsc-cert-gen.json")) as f:
		j = load(f)
	cleanup()
	return j["event_name"]

eel.start("index.html")
