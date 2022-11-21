import csv

with open("sample.csv", "w") as file_object:
    # ①csv.DictWriterの第2引数にリストを指定する
    dw_object = csv.DictWriter(file_object, ["A", "B", "C"])

    # ② writeheader()を実行すると①で指定したリストの要素がヘッダーとして書き込まれる
    dw_object.writeheader()

    # ③キーと値をセットで書き込む
    dw_object.writerow({"A": 1, "B": 2, "C": 3})

    # ④キーと値を指定しないこともできる
    dw_object.writerow({"A": 4, "B": 5})

    # ⑤エラーになる
    dw_object.writerow({"D": 4, "B": 5, "C": 6})
    dw_object.writerow({"": 4, "B": 5, "C": 6})


# ⑥ここから読み込み（書き込まれたことの確認）
with open("sample.csv") as file_object:
    print(file_object.read())
# ⑦:　①〜④までの出力結果
# A,B,C
# 1,2,3
# 4,5,
