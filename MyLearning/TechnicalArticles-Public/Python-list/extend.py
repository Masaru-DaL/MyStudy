sample_list1 = ["A", "B"]
sample_list2 = ["E", "F"]

# ①
sample_list1.extend("CD")
print(sample_list1)
# 出力結果: ['A', 'B', 'C', 'D']

# ②
sample_list1.extend(sample_list2)
print(sample_list1)
# 出力結果: ['A', 'B', 'C', 'D', 'E', 'F']

# ③
sample_list3 = sample_list1.extend(sample_list2)
print(sample_list3)
# 出力結果: None
