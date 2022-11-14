sample_list = ["A", "B", "C", "D", "E"]

# ①要素Eを指定
print(sample_list.index("E"))
# 出力結果: 4

# ②存在しないXを指定
print(sample_list.index("X"))
# 出力結果: ValueError: 'X' is not in list
