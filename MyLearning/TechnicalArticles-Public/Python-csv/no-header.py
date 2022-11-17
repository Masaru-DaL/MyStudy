import csv
import pprint

with open("sample.csv") as file_object:
    dict_reader_object = csv.DictReader(file_object)

    sample_dict = [row for row in dict_reader_object]

# ①
pprint.pprint(sample_dict)
# 出力結果:
# [{'1': '5', '2': '6', '3': '7', '4': '8'},
#  {'1': '9', '2': '10', '3': '11', '4': '12'}]
