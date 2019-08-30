import eel
from file_handler import getFile
from program import start, join, loadEditor
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
		return False

@eel.expose
def setupEditor():
	j = loadEditor()
	return [j["event_name"], [j["template"], j["width"], j["height"]], read_csv(j["csv"], only_cols=True)]

eel.start("index.html")
