import csv

def read_dict_csv(path):
    with open (path, 'r') as f:
        data = []
        file = csv.DictReader(f)
        for row in file:
            data.append(dict(row))
    return data

def writer_dict_csv(path, data):
    assert data != []
    with open (path, 'w') as f:
        file = csv.DictWriter(f, fieldnames=data[0].keys())
        file.writerows(data)


if __name__ == "__main__":
    print("Glory to Ukraine!")