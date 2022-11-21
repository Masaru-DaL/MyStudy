import csv

# ①書き込む二次元リストを用意
write_list = [[1, 2, 3], ["A", "B", "CD"], ["E,F,G", "H", "I"]]

# ②ここから書き込み
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object, quoting=csv.QUOTE_ALL)
    writer_object.writerows(write_list)

# ③ここから読み込み（書き込まれたことの確認）
with open("sample.csv") as file_object:
    print(file_object.read())

# ④出力結果:
# "1","2","3"
# "A","B","CD"
# "E,F,G","H","I"
