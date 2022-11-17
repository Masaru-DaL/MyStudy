import csv
import pprint

with open("sample.csv") as file_object:
    # ②headerにA,B,C,Dを指定する
    dict_reader_object = csv.DictReader(file_object, fieldnames=["A", "B", "C", "D"])

    sample_dict = [row for row in dict_reader_object]

# ③
pprint.pprint(sample_dict)
# 出力結果:
# [{'A': '1', 'B': '2', 'C': '3', 'D': '4'},
#  {'A': '5', 'B': '6', 'C': '7', 'D': '8'},
#  {'A': '9', 'B': '10', 'C': '11', 'D': '12'}]
