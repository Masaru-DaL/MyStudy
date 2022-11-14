import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①
    sample_list = [row for row in reader_object]

# ①
print(sample_list[0][0])
print(sample_list[2][3])

# 出力結果:
# 1
#  12（先頭の空白は、sample.csvに空白があるため）
