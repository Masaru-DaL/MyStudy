sample_list1 = [1, 2, 3, 4]

# ③リスト内包表記を使用して一次元リストを取得
new_sample_list1 = [i for i in sample_list1]
print(new_sample_list1)
# 出力結果: [1, 2, 3, 4]


sample_list2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

# ③リスト内包表記を使用して二次元リストを取得
new_sample_list2 = [i for row in sample_list2 for i in row]
print(new_sample_list2)
# 出力結果: [1, 2, 3, 4, 5, 6, 7, 8]
