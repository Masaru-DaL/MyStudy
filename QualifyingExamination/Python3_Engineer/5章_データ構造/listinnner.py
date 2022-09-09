data = []  # 空のリストを宣言
for i in range(10):
    data.append(i)

# step1(空のリストを宣言)
data = []

# step2(for i in ~をリスト内に持ってくる)
data = [for i in range(10)]

# step3(追加する値iを先頭に書く)
data = [i for i in range(10)]
