import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①特定の列を取得する
    sample_list1 = [row[0] for row in reader_object]
    print(sample_list1)
    # 出力結果: ['1', '5', '9', '13', '17']

# ②違う列を取得するためにはもう一度ファイル操作から行う
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    sample_list2 = [row[3] for row in reader_object]
    print(sample_list2)
    # 出力結果: [' 4', ' 8', ' 12', ' 16', ' 20']
