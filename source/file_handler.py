import codecs
from os.path import basename
from tkinter import Tk, filedialog
from xlrd import open_workbook
from os.path import basename

def getFile(type_):
	root = Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	if type_ == "template":
		filename =  filedialog.askopenfilename(title="Select Template", filetypes = (("images","*.jpg *.png *.jpeg *.tif *.tiff *.bmp"), ("all files","*.*")))
	if type_ == "csv":
		filename =  filedialog.askopenfilename(title="Select SpreadSheet File", filetypes = (("spreadsheet","*.csv *.xlsx *.xls"), ("all files","*.*")))
	return [filename, basename(filename)]

# Reading CSV files
def read_csv(filename, delimeter=",", only_cols=False):
    with codecs.open(filename, "r", "utf-8") as f:
        csv_raw_data = f.read().strip().split("\n")

    columns = csv_raw_data[0].split(delimeter)
    if only_cols:
        return columns

    csv_data = []
    for csv in csv_raw_data[1:]:
        csv_data.append(csv.split(delimeter))

    return csv_data, columns

# Reading excel files
def read_excel(filename, only_cols=False):
    wb = open_workbook(filename)
    values = []
    for s in wb.sheets():
        for row in range(s.nrows):
            col_names = s.row(row)
            row_val = []
            for _ in col_names:
                row_val.append(_.value)
            values.append(row_val)
    if only_cols:
        return values[0]

    return values[1:], values[0]

def read_data(filename, only_cols=False):
    if basename(filename).lower().split(".")[-1] == "csv":
        cols = read_csv(filename, only_cols=only_cols)
    else:
        cols = read_excel(filename, only_cols=only_cols)
    return cols
