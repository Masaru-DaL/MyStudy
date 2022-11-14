sample_list = ["E", "D", "C", "B", "A"]

# ①昇順に整列
sorted(sample_list)
print(sample_list)
# 出力結果: ['A', 'B', 'C', 'D', 'E']

# ②降順に整列
sorted(sample_list, reverse=True)
print(sample_list)
# 出力結果: ['E', 'D', 'C', 'B', 'A']

# ③昇順に整列した結果を新しいリスト変数に格納する
new_sample_list = sorted(sample_list)
print(new_sample_list)
# 出力結果: ['A', 'B', 'C', 'D', 'E']
