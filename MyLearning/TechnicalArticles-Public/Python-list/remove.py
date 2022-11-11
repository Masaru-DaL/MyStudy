sample_list = ["A", "B", "B", "D", "E"]

# ①
sample_list.remove("A")
print(sample_list)
# 出力結果: ['B', 'C', 'D', 'E']

# ②
sample_list.remove("B")
print(sample_list)
# 出力結果: ['B', 'D', 'E']

# ③存在しない要素を指定する
sample_list.remove("Z")
print(sample_list)
# 出力結果: ValueError: list.remove(x): x not in list
