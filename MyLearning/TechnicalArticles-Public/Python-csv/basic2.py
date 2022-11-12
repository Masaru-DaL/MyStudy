import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    
    # ①
    two_dimensions_list = [row for row in reader_object]

print(two_dimensions_list)
# 出力結果:
# [['1', ' 2', ' 3', ' 4'], ['5', ' 6', ' 7', ' 8']]
