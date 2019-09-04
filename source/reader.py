import codecs
from xlrd import open_workbook

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

print(read_excel("C:\\Users\\LordGhostX\\Desktop\\Book1.xlsx"))
