import csv

# ①書き込む二次元リストを用意
write_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# ②ここから書き込み
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerows(write_list)

# ③書き込まれた内容の確認
with open("sample.csv") as file_object:
    print(file_object.read())

# ④出力結果:
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12
