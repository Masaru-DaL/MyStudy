import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①
    two_dimensions_list = [row for row in reader_object]

# ①
print(two_dimensions_list[0][0])
print(two_dimensions_list[2][3])

# 出力結果:
# 1
#  12
