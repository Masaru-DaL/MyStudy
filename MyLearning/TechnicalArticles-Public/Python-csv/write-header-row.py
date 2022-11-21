import csv
import pprint

# ①見出し行を別に用意する
write_header = ["A", "B", "C", "D", "E"]

# ②まずは既存のファイルを読み込んで2次元リストに格納する
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    sample_list = [row for row in reader_object]

# ③2次元リストの確認
pprint.pprint(sample_list)
# [['1', '2', '3', '4', '5'],
#  ['6', '7', '8', '9', '10'],
#  ['11', '12', '13', '14', '15']]

# ④既存のファイルを上書きする形で、新規作成で開く
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    # ⑤見出し行->既存のファイルデータの順で書き込む
    writer_object.writerow(write_header)
    writer_object.writerows(sample_list)

with open("sample.csv") as file_object:
    print(file_object.read())

# ⑥出力結果: 最終的なsample.csvの中を確認
# A,B,C,D,E
# 1,2,3,4,5
# 6,7,8,9,10
# 11,12,13,14,15
