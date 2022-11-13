import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①
    two_dimensions_list = [row for row in reader_object]

# ①index指定
print(two_dimensions_list[0])
print(two_dimensions_list[-1])
# 出力結果:
# ['1', ' 2', ' 3', ' 4']
# ['9', ' 10', ' 11', ' 12']

# ②スライス
print(two_dimensions_list[3:])
print(two_dimensions_list[0:2])
# 出力結果:
# [['13', ' 14', ' 15', ' 16'], ['17', ' 18', ' 19', ' 20']]
# [['1', ' 2', ' 3', ' 4'], ['5', ' 6', ' 7', ' 8']]
