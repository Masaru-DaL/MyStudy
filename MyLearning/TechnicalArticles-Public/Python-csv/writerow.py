import csv

# ①ここから書き込み
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerow([1, 2, 3])
    writer_object.writerow(["A", "B", "C"])

# ②書き込まれた内容の確認
with open("sample.csv") as file_object:
    print(file_object.read())

# ③出力結果:
# 1,2,3
# A,B,C
