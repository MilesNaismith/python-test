import csv
a = list()
with open("log.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(a)