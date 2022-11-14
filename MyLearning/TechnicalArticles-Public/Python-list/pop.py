sample_list = ["A", "B", "C", "D", "E"]

# ①index0を指定
print(sample_list.pop(0))
print(sample_list)
# 出力結果:
# A
# ['B', 'C', 'D', 'E']

# ②indexの指定を省略
sample_list.pop()
print(sample_list)
# 出力結果: ['B', 'C', 'D']

# ③存在しないindexを指定
sample_list.pop(4)
# 出力結果: IndexError: pop index out of range
