import csv

# ①ここから書き込み
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    writer_object.writerow([1, 2, 3])
    writer_object.writerow(["A", "B", "C"])

# ②ここから読み込み（書き込まれたことを確認）
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    for row in reader_object:
        print(row)

# ③出力結果:
# ['1', '2', '3']
# ['A', 'B', 'C']
