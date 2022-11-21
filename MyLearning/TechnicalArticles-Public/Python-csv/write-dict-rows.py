import csv

dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"A": 4, "B": 5, "C": 6}
dict3 = {"A": 7, "C": 9}


with open("sample.csv", "w") as file_object:
    dw_object = csv.DictWriter(file_object, ["A", "B", "C"])
    dw_object.writeheader()

    # ①
    dw_object.writerows([dict1, dict2, dict3])


# ②ここから読み込み（書き込まれたことの確認）
with open("sample.csv") as file_object:
    print(file_object.read())
# ③出力結果:
# A,B,C
# 1,2,3
# 4,5,6
# 7,,9
