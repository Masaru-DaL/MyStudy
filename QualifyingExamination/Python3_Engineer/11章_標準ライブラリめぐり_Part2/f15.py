import bisect

# ソートしている場合
scores1 = [1, 2, 4]
bisect.insort(scores1, 3)
print(scores1)

# ソートしていない場合
scores2 = [12, 11, 14]
bisect.insort(scores2, 13)
print(scores2)

# 一度ソートする
scores3 = [12, 11, 14]
scores3.sort()
bisect.insort(scores3, 13)
print(scores3)
