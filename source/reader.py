import codecs

# Reading CSV files
def read_csv(filename, delimeter=",", only_cols=False):
    with codecs.open(filename, "r", "utf-8") as f:
        csv_raw_data = f.read().strip().split("\n")
    csv_data = []
    for csv in csv_raw_data[1:]:
        csv_data.append(csv.split(delimeter))
    columns = csv_raw_data[0].split(delimeter)

    if only_cols:
        return columns
    return csv_data, columns
