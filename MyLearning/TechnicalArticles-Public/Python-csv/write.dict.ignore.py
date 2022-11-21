import csv

dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"A": 4, "B": 5, "C": 6}
dict3 = {"A": 7, "B": 8, "C": 9}


with open("sample.csv", "w") as file_object:
    # ①第二引数には書き込みたいキー
    # ②引数extrasactionをignoreに指定
    dw_object = csv.DictWriter(file_object, ["A", "C"], extrasaction="raise")

    # ③エラーになるパターン
    # dw_object = csv.DictWriter(file_object, ["A", "C"])

    dw_object.writeheader()
    dw_object.writerows([dict1, dict2, dict3])


# ④ここから読み込み（書き込まれたことの確認）
with open("sample.csv") as file_object:
    print(file_object.read())
# ⑤出力結果:
# A,C
# 1,3
# 4,6
# 7,9
