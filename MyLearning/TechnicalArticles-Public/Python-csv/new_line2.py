import csv

with open("sample.csv", newline="", encoding="UTF-8") as file_object:
    reader_object = csv.reader(file_object, delimiter=" ")

    for row in reader_object:
        print(row)
