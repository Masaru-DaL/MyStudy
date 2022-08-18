# カードがN枚
# 一番上が1 一番下がN(9)

# 上からM枚事のセットに分ける
# 一番下がM枚未満の場合はM枚未満のまま1つのセットとする

# もし3つに分けた場合
# setA, setB, setC -> setC, setB, setAに分ける
# この操作を1セットとする

## 入力値に関して
# A B C というフォーマットで入力される
# A -> カード枚数を表す整数
# B -> 1セットあたりの枚数を表す整数
# C -> シャッフルの回数を表す整数
# 入力例 -> 9 3 1

# coding: utf-8

# カード枚数 -> card_num
# 1セットの枚数 -> set_num
# シャッフルの回数 -> shuffle_num

# coding: utf-8

# カード枚数 -> card_num
# 1セットの枚数 -> set_num
# シャッフルの回数 -> shuffle_num

card_num, set_num, shuffle_num = map(int, input().split())

card_list = list(range(0, card_num+1))

shuffle_list = []
for i in range(1, len(card_list), set_num):
    set_list = list(card_list[i: i+set_num])
    shuffle_list.append(set_list)

result_list = []

for i in range(shuffle_num):
    result_list = sorted(shuffle_list, reverse=True)

for i in result_list:
    for j in i:
        print(j)
