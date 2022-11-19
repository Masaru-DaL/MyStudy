import csv
import pprint

# ①書き込む二次元リストを用意
write_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# ②ここから書き込み
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerows(write_list)

# ③ここから読み込み（書き込まれたことの確認）
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    sample_list = [row for row in reader_object]

pprint.pprint(sample_list, width=40)
# ④出力結果:
# [['1', '2', '3', '4'],
#  ['5', '6', '7', '8'],
#  ['9', '10', '11', '12']]
