import eel
from file_handler import getFile

eel.init("UI")

g_event_name, g_template, g_csv = None, None, None

@eel.expose
def getTemplate():
	return getFile("template")

@eel.expose
def getCSV():
	return getFile("csv")

@eel.expose
def startProgram(event_name, template, csv):
	if event_name and template and csv:
		g_event_name, g_template, g_csv = event_name, template, csv
		return True
	else:
		return False

eel.start("index.html")
