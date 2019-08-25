# Main python file; Run this
from csv_reader import read_csv
from generator import generator
import matplotlib.pyplot as plt

locations = []

def onclick(event):
    x = event.xdata
    y = event.ydata
    plt.scatter(x, y)
    locations.append([x, y])
    plt.show()

# Get all necessary inputs from the user
filename = input("Enter CSV filename: ")
csv_data, columns, emails = read_csv(filename)

additional_n = int(input("Your data has {} columns; If you have static data to add enter the number (Enter 0 if you have none): ".format(len(columns) - 1)))
additional_data = []
print("Enter your static data: ")
for _ in range(additional_n):
    additional_data.append(input("::: "))

csv_data = [(data + additional_data) for data in csv_data]

template_name = input("Enter the Template path: ")

im = plt.imread(template_name)
fig, ax = plt.subplots()
ax.plot(0)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.imshow(im)
plt.title("Click the {} points on the image".format(len(csv_data[0])))
plt.xlabel("Exit the editor to start the generation...")
plt.show()

for data in range(len(csv_data)):
    print("Editing", csv_data[data][0], "Certificate")
    generator(template_name, csv_data[data], locations, emails[data], font=None, font_size=None, font_color=(0, 0, 0))

print("Done!")
