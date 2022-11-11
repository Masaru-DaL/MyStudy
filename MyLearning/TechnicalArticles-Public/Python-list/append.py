sample_list = ["a", "b", "c", "d", "e"]

# ①
sample_list.append("f")
print(sample_list)
# 出力結果: ['a', 'b', 'c', 'd', 'e', 'f']

# ②
sample_list.append("100")
print(sample_list)
# 出力結果: ['a', 'b', 'c', 'd', 'e', 'f', '100']
