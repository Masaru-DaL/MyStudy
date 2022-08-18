# coding: utf-8

peopel_num, right_num = map(int, input().split())

# 正しい音程の曲をリストに入れる
right_list = []
for i in range(right_num):
    right_list.append(int(input()))

right_list = right_list * peopel_num

# 2人分のポイントをリストに格納
point_list = []
for i in range(peopel_num * right_num):
    point_list.append(int(input()))

test_list = []

for i in range(len(point_list)):
    point = right_list[i] - point_list[i]
    if point < 0:
        point = point * -1

    if 0 <= point <= 5:
        test_list.append(0)

    elif 5 < point <= 10:
        test_list.append(1)
    elif 10 < point <= 20:
        test_list.append(2)
    elif 20 < point <= 30:
        test_list.append(3)
    else:
        test_list.append(5)

result_list = []

if peopel_num >= 2:
    for i in range(0, len(test_list), right_num):
        result_point = test_list[i: i+right_num]
        result_point = sum(result_point)
        result_point = 100 - result_point

        if result_point < 0:
            result_point = result_point * -1
            result_list.append(int(result_point))
        else:
            result_list.append(int(result_point))
    max_point = max(result_list)
    print(max_point)
elif peopel_num <= 1:
    result_point = sum(test_list)
    if result_point > 100:
        print(0)
