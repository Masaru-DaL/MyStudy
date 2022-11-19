import csv
import pprint

# ①書き込む二次元リストを用意
write_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# ②ここから書き込み
with open("sample.tsv", "w") as file_object:
    # ③空白区切りを指定
    writer_object = csv.writer(file_object, delimiter="\t")
    writer_object.writerows(write_list)

# ④ここから読み込み（書き込まれたことの確認）
with open("sample.tsv") as file_object:
    reader_object = csv.reader(file_object)

    sample_list = [row for row in reader_object]

pprint.pprint(sample_list, width=40)
# ⑤出力結果:
# [['1 2 3 4'],
#  ['5 6 7 8'],
#  ['9 10 11 12']]
