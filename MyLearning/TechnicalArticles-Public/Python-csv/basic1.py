import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    # ①
    print(reader_object)

    # ②
    for row in reader_object:
        print(row)
