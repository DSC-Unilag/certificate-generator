import eel
from os.path import basename
from tkinter import Tk, filedialog

eel.init("UI")

@eel.expose
def getTemplate():
	return getFile("template")

@eel.expose
def getCSV():
	return getFile("csv")

def getFile(type_):
	root = Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	if type_ == "template":
		filename =  filedialog.askopenfilename(title="Select Template", filetypes = (("images","*.jpg *.png *.jpeg *.tif *.tiff *.bmp"), ("all files","*.*")))
	if type_ == "csv":
		filename =  filedialog.askopenfilename(title="Select CSV File", filetypes = (("CSV file","*.csv"), ("all files","*.*")))
	return [filename, basename(filename)]

eel.start("index.html")
