import csv
import pprint # データ整形のために使用

with open("sample.csv") as file_object:
    reader_object = csv.reader(file_object, skipinitialspace=True)

    # ①headerを含む全てのCSVファイルを取得
    sample_list = [row for row in reader_object]

pprint.pprint(sample_list)
# 出力結果:
# [['', ' Bob', ' Lisa', ' Mike', ' Alisa'],
#  ['Math', ' 70', ' 30', ' 80', ' 60'],
#  ['English', ' 90', ' 85', ' 50', ' 70'],
#  ['Science', ' 80', ' 100', ' 50', ' 80'],
#  ['Japanese', ' 80', ' 70', ' 90', ' 85']]

# ② ①から数値データ部分のみを取得する
pprint.pprint([row [1:] for row in sample_list[1:]])
# 出力結果:
# [[' 70', ' 30', ' 80', ' 60'],
#  [' 90', ' 85', ' 50', ' 70'],
#  [' 80', ' 100', ' 50', ' 80'],
#  [' 80', ' 70', ' 90', ' 85']]

# ③ ①から数値データ部分を抽出する時点でint型に変換する
print([[int(i) for i in row[1:]] for row in sample_list[1:]])
# 出力結果:
# [[70, 30, 80, 60], [90, 85, 50, 70], [80, 100, 50, 80], [80, 70, 90, 85]]
