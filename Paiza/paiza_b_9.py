## 入力値
# A B C D
# A -> 発言の件数
# B -> 監視する時間
# C -> バズ判定における対象期間
# D -> GOODアクションの回数

# 発言がA件
# 各発言をB時間監視する
# 1時間ごとにGOODアクションの増分を計測する
# C時間以内にD回以上GOODが起こった発言をバズっているとする

# C時間以内にD回以上GOODが起こった発言を全て検出するプログラムを作成すう
# 各発言(バズった)が初めてバズっていると判定されたタイミングも求める

# 2 5 3 1000
# 100 100
# 500 200
# 60 300
# 100 500
# 10 1000

# coding: utf-8
import sys
input = sys.stdin.readline

# comments_number -> 発言の件数
# check_time -> 監視する時間
# monitoring_time -> バズ判定における対象期間
# good_number -> GOODアクションの回数

comments_number, check_time, monitoring_time, good_number = map(int, input().split())
# print(comments_number, check_time, monitoring_time, good_number)

good_count_list = []
for i in range(check_time):
    count_list = list(input().split())
    # print(count_list)
    good_count_list.append(count_list)

# print(good_count_list)
good_count_list_all = []

for i in range(len(good_count_list[0])):
    tmp = []
    for v in good_count_list:
        tmp.append(int(v[i]))
    good_count_list_all.append(tmp)

# print(good_count_list_all)
count = 1
point = 0
clear_count = 0

for i in range(len(good_count_list_all)):
    for j in good_count_list_all[i]:
        point = point + j
        if clear_count == check_time:
            count = 0
            point = 0
        elif clear_count > 0:
                point = point + j
                clear_count += 1

        elif count <= check_time and point >= good_number:
            clear_count = count
            print("yes " + str(clear_count))



        elif count == check_time and point < good_number:
            print("no 0")
            point = 0
            count = 0
        elif count == check_time:
            count = 0
            point = 0
        count += 1


# for i in range(len(good_count_list_all)):
#     point += good_count_list_all
# print(good_count_list_all[0])
# print(good_count_list_all[1])

# for i in good_count_list_all:
    # i = (sum(i))

    # if i >= 1000:
    #     print(count)
    # else:
    #     print("no 0")
    # i += i
    # i = sum(i)
    # print(i)
    # if count == check_time:

    # count += 0
# for i in good_count_list_all:
#     for j in i:
#         if count == check_time:

#         count += 1





        