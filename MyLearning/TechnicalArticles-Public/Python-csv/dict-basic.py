import csv
import pprint

with open("sample.csv") as file_object:
    # ①csv.DictReaderの引数にファイルオブジェクトを渡す
    dict_reader_object = csv.DictReader(file_object)

    sample_dict = [row for row in dict_reader_object]

# ②
pprint.pprint(sample_dict)
# 出力結果:
# [{'A': '1', 'B': '2', 'C': '3', 'D': '4'},
#  {'A': '5', 'B': '6', 'C': '7', 'D': '8'}]
