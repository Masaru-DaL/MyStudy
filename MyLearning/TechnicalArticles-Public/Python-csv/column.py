import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    # ①特定の列を取得する
    column_list_index0 = [row[0] for row in reader_object]
    print(column_list_index0)
    # 出力結果: ['1', '5', '9', '13', '17']

# ②
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    column_list_index3 = [row[3] for row in reader_object]
    print(column_list_index3)
    # 出力結果: [' 4', ' 8', ' 12', ' 16', ' 20']


    # # ①二次元リストの取得
    # row_list = [row for row in reader_object]

    # # ②行と列を入れ替える（転置）
    # column_list = [list(x) for x in zip(*row_list)]
    # print(column_list)
    # # 出力結果: （可読性のため改行してます）
    # # [['1', '5', '9', '13', '17'],
    # # [' 2', ' 6', ' 10', ' 14', ' 18'],
    # # [' 3', ' 7', ' 11', ' 15', ' 19'],
    # # [' 4', ' 8', ' 12', ' 16', ' 20']]

    # # ③特定の列を取得
    # print(column_list[0])
    # print(column_list[3])
    # # 出力結果:
    # # ['1', '5', '9', '13', '17']
    # # [' 4', ' 8', ' 12', ' 16', ' 20']
