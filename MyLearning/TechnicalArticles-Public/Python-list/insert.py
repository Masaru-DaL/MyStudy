sample_list = ["A", "B", "C"]

# ①index1を指定してい"X"を挿入
sample_list.insert(1, "X")
print(sample_list)
# 出力結果: ['A', 'X', 'B', 'C']

# ②リストの末を指定して"Y"を挿入
sample_list.insert(-1, "Y")
print(sample_list)
# 出力結果: ['A', 'X', 'B', 'Y', 'C']

# ③存在しないindexを指定して、"Z"を挿入
sample_list.insert(5, "Z")
print(sample_list)
# 出力結果: ['A', 'X', 'B', 'Y', 'C', 'Z']
