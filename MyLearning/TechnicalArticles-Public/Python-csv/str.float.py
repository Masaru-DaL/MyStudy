import csv

with open("sample.csv") as file_object:
    # ①全てのフィールドをfloat型にする
    reader_object = csv.reader(file_object, quoting=csv.QUOTE_NONNUMERIC)

    sample_list = [row for row in reader_object]

# ②CSVファイルの最初の行をfloat型に変換する
print(sample_list[0][0])
print(type(sample_list[0][0]))
# 出力結果:
# 1.1
# <class 'float'>



# import csv

# with open("sample.csv") as file_object:
#     # ①全てのフィールドをfloat型にする
#     reader_object = csv.reader(file_object)

#     sample_list = [row for row in reader_object]

# # ②CSVファイルの最初の行をfloat型に変換する
# float_list = [float(i) for i in sample_list[0]]
# print(float_list)
# print(type(float_list[0]))
# # 出力結果:
# # [1.2, 1.2, 1.3, 1.4]
# # <class 'float'>

# # ③二次元リストを一気にint型に変換する
# print([[float(i) for i in row] for row in sample_list])
# # 出力結果:
# # [[1.2, 1.2, 1.3, 1.4], [1.5, 1.6, 1.7, 1.8]]
