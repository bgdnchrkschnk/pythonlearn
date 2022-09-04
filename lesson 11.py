import csv

path = "test.csv"
def read_csv(path):
    with open(path, "r") as f:
        data = []
        file_csv = csv.reader(f)
        for row in file_csv:
         data.append(row)
    print(data)
read_csv(path)