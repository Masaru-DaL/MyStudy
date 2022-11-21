import csv

# ①追記モードで書き込み
with open("sample.csv", "a") as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerow([4, 5, 6])
    writer_object.writerow(["D", "E", "F"])

# ②書き込まれた内容の確認
with open("sample.csv") as file_object:
    print(file_object.read())

# ③出力結果:
# 1,2,3
# A,B,C
# 4,5,6
# D,E,F
