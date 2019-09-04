from os.path import basename
from tkinter import Tk, filedialog

def getFile(type_):
	root = Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	if type_ == "template":
		filename =  filedialog.askopenfilename(title="Select Template", filetypes = (("images","*.jpg *.png *.jpeg *.tif *.tiff *.bmp"), ("all files","*.*")))
	if type_ == "csv":
		filename =  filedialog.askopenfilename(title="Select SpreadSheet File", filetypes = (("spreadsheet","*.csv *.xlsx *.xls"), ("all files","*.*")))
	return [filename, basename(filename)]
