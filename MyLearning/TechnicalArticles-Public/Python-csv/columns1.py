import csv

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)

    sample_list = [row for row in reader_object]

    # ①行と列を入れ替える（転置）
    columns_list = [list(x) for x in zip(*sample_list)]
    print(columns_list)
    # 出力結果: （可読性のため改行してます）
    # [['1', '5', '9', '13', '17'],
    # [' 2', ' 6', ' 10', ' 14', ' 18'],
    # [' 3', ' 7', ' 11', ' 15', ' 19'],
    # [' 4', ' 8', ' 12', ' 16', ' 20']]

    # ②特定の列を取得
    print(columns_list[0])
    print(columns_list[3])
    # 出力結果:
    # ['1', '5', '9', '13', '17']
    # [' 4', ' 8', ' 12', ' 16', ' 20']
