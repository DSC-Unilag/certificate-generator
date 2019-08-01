# This handles reading the CSV file

def read_csv(filename):
    # Read it as a normal file
    with open(filename, "r") as f:
        # Strip additional lines so it does not run into errors later on then split by new line so we know each line is a different row
        csv_raw_data = f.read().strip().split("\n")

    csv_data = []
    for csv in csv_raw_data[1:]:
        csv_data.append(csv.split(","))

    columns = csv_raw_data[0].split(",")

    # We are returning a list of all names
    return csv_data, columns
