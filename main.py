# Main python file; Run this
from csv_reader import read_csv
from generator import generator

# Get all necessary inputs from the user
filename = input("Enter CSV filename: ")
template_name = input("Enter Template filename: ")
program_name =  input("Enter Program Name: ")
certification_date = input("Enter Certification Date: ")

names = read_csv(filename)

for name in names:
    print("Editing", name, "Certificate")
    generator(name, template_name)

print("Done!")
