# This handles reading the CSV file

def read_csv(filename):
    # Read it as a normal file
    with open(filename, "r") as f:
        # Strip additional lines so it does not run into errors later on then split by new line so we know each line is a different name
        csv = f.read().strip().split("\n")
        
    #We are returning a list of all names
    return csv
