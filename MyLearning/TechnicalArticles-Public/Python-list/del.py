sample_list = ["A", "B", "C", "D", "E"]

# ①index0を指定
del sample_list[0]
print(sample_list)
# 出力結果: ['B', 'C', 'D', 'E']

# ②index1~-1の1個前まで
del sample_list[1:-1]
print(sample_list)
# 出力結果: ['B', 'E']

# ③リスト自体を削除
del sample_list
print(sample_list)
# 出力結果: 
