import csv

with open("sample.csv", encoding="UTF-8") as file_object:
    # ①csv.readerの引数にquoting=csv.QUOTE_NONEを指定
    reader_object = csv.reader(file_object, delimiter=" ", quoting=csv.QUOTE_NONE)

    for row in reader_object:
        print(row)

# 出力結果:
# ['商品', '単価', '数量']
# ['A商品', '500', '1']
# ['B商品', '900', '3']
# ②['"Python', 'csvの本"', '1500', '1']
