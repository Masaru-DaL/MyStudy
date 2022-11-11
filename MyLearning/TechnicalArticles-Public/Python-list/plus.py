sample_list1 = ["A", "B"]
sample_list2 = ["E", "F"]

# ①
sample_list1 + "CD"
print(sample_list1)
# 実行結果: TypeError: can only concatenate list (not "str") to list

# ②
sample_list1 + sample_list2
print(sample_list1)
print(sample_list2)
# 出力結果: ['A', 'B']
# 出力結果: ['E', 'F']

# ③
sample_list3 = sample_list1 + sample_list2
print(sample_list3)
# 出力結果: ['A', 'B', 'E', 'F']
