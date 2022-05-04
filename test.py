import csv
with open('C:\\Users\\zumie\\Documents\\GitHub\\fuzzy-succotash\\data\\ep.csv') as episode:
    csv = csv.reader(episode, delimiter=",")
    for row in episode:
        print(row)


# dictionary possibly