import csv
import pprint

with open("sample.csv") as file_object:
    dict_reader_object = csv.DictReader(file_object)

    sample_dict = [row for row in dict_reader_object]

# ③
pprint.pprint(sample_dict)
# 出力結果:
# [{'': 'Bob', 'A': '80', 'B': '70', 'C': '90', 'D': '100'},
# {'': 'Lisa', 'A': '90', 'B': '100', 'C': '70', 'D': '80'},
#  {'': 'Alisa', 'A': '70', 'B': '80', 'C': '100', 'D': '100'}]

print([header_column.pop])
