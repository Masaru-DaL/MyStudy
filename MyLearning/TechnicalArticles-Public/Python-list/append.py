sample_list = ["a", "b", "c"]

# ①
sample_list.append("d")
print(sample_list)
# 出力結果: ['a', 'b', 'c', 'd']

# ②
sample_list.append(["e", "f"])
print(sample_list)
# 出力結果: ['a', 'b', 'c', 'd', ['e', 'f']]

# ③
sample_list.append("100")
print(sample_list)
# 出力結果: ['a', 'b', 'c', 'd', ['e', 'f'], '100']
