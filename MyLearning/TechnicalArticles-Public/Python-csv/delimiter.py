import csv

with open("sample.csv") as file_object:
    # ①区切り文字を空白に指定
    reader_object = csv.reader(file_object, delimiter=" ")

    sample_list = [row for row in reader_object]

print(sample_list)
