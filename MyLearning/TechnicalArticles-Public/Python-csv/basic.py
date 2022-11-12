import csv

with open("sample.csv") as rf:
    reader_object = csv.reader(rf)
    # ①
    print(reader_object)

    # ②
    for row in reader_object:
        print(row)
