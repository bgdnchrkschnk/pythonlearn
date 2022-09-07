import csv

# path = "test.csv"
# def read_csv(path):
#     with open(path, "r") as f:
#         data = []
#         file_csv = csv.reader(f)
#         for row in file_csv:
#          data.append(row)
#     print(data)
# read_csv(path)
import random


# def read_csv(path):
#     data = []
#     with open (path, 'r') as f:
#         file = csv.reader(f)
#         for row in file:
#             data.append(row)
#     return data
#
# data = read_csv("persons.csv")

# for row in data[1:]:
#     row[1] = int(row[1]) + 100
#
# data[0].append("Education")
# for row in data[1:]:
#     row.append(random.choice([0,1]))

def read_dict_csv(path):
    with open (path, 'r') as f:
        data = []
        file = csv.DictReader(f)
        for row in file:
            data.append(dict(row))
    return data
data = read_dict_csv("persons.csv")
for row in data:
    row['Education'] = random.choice([0,1])
print(data)

# def writer_csv(path, data):
#     with open (path, 'w') as f:
#         file = csv.writer(f)
#         file.writerows(data)
#
# read_csv("persons.csv")
# writer_csv("persons_futuristic.csv", data)

