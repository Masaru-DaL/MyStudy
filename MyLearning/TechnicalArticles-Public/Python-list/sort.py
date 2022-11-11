sample_list = ["A", "B", "C", "D", "E"]

# ①降順に整列
sample_list.sort(reverse=True)
print(sample_list)
# 出力結果: ['E', 'D', 'C', 'B', 'A']

# ②
print(sample_list.sort(reverse=True))
# 出力結果: None

# ③
new_sample_list = sample_list.sort(reverse=True)
print(new_sample_list)
# 出力結果: None

# ②昇順に整列
sample_list.sort()
print(sample_list)
# 出力結果: ['A', 'B', 'C', 'D', 'E']
