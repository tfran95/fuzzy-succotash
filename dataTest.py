import csv
with open('C:\\Users\\zumie\\Documents\\GitHub\\fuzzy-succotash\\data\\ep.csv') as csv_file:
    csv = csv.reader(csv_file, delimiter=",")

    for row in csv_file:
        print(row)