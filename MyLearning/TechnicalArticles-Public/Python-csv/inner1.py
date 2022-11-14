sample_list1 = [1, 2, 3, 4]
new_sample_list1 = []

# ①一次元リストの取得
for i in sample_list1:
    new_sample_list1.append(i)

print(new_sample_list1)
# 出力結果: [1, 2, 3, 4]


sample_list2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_sample_list2 = []

# ②二次元リストの取得
for row in sample_list2:
    for i in row:
        new_sample_list2.append(i)

print(new_sample_list2)
# 出力結果: [1, 2, 3, 4, 5, 6, 7, 8]
