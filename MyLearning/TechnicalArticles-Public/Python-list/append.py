sample_list = ["A", "B", "C"]

# ①
sample_list.append("D")
print(sample_list)
# 出力結果: ['A', 'B', 'C', 'D']

# ②
sample_list.append(["E", "F"])
print(sample_list)
# 出力結果: ['A', 'B', 'C', 'D', ['E', 'F']]

# ③
sample_list.append("100")
print(sample_list)
# 出力結果: ['A', 'B', 'C', 'D', ['E', 'F'], '100']
