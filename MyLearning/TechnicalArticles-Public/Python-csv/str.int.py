import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①二次元リストを取得
    sample_list = [row for row in reader_object]

# ②取り出した要素の型を確認する
print(sample_list[0][0])
print(type(sample_list[0][0]))
# 出力結果:
# 1
# <class 'str'>

# ③CSVファイルの最初の行をint型に変換する
int_list = [int(i) for i in sample_list[0]]
print(int_list)
print(type(int_list[0]))
# 出力結果:
# [1, 2, 3, 4]
# <class 'int'>

# ④二次元リストを一気にint型に変換する
print([[int(i) for i in row] for row in sample_list])
# 出力結果:
# [[1, 2, 3, 4], [5, 6, 7, 8]]
