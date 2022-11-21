import csv
import pprint

# ①見出し列を用意する
write_index = ["Math","Japanese","Science","English"]

# ②既存のファイルを読み込んで2次元リストに格納する
with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object)
    sample_list = [row for row in reader_object]

# ③2次元リストの確認
pprint.pprint(sample_list)
# [["''", 'Bob', 'Lisa', 'Mike', 'Alisa'],
#  ['70', '30', '80', '60'],
#  ['90', '85', '50', '70'],
#  ['80', '100', '50', '80'],
#  ['80', '70', '90', '85']]


# ④既存のファイルを上書きする形で、新規作成で開く
with open("sample.csv", "w") as file_object:
    writer_object = csv.writer(file_object)
    # ⑤見出し行を書き込む
    writer_object.writerow(sample_list[0])
    # ⑥見出し列を先頭に加えながら、残りの2次元リストを書き込む
    for i, row in zip(write_index, sample_list[1:]):
        writer_object.writerow([i] + row)

with open("sample.csv") as file_object:
    print(file_object.read())

# ⑦出力結果: 最終的なsample.csvの中を確認
# '',Bob,Lisa,Mike,Alisa
# Math,70,30,80,60
# Japanese,90,85,50,70
# Science,80,100,50,80
# English,80,70,90,85
