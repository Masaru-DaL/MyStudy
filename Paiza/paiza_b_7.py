### 入力値 N M
# N -> 回答者の数
# M -> 訪問(解答)した回数
## 2行目以降

# 0以上100以下の整数ではないデータ全てを削除する
# 先頭に0は有効
# クレンジングする際に、削除したデータ箇所には0を代入する
# クレンジング後、回答の平均を小数点以下を切り捨てて出力

# coding: utf-8
import sys
import math

peopel_num, responce_num = map(int, input().split())

result_list = []

for i in range(peopel_num):
    responce_list = list(input().split())
    result_list.append(responce_list)

cleansing_list = []

for i in result_list:
    for j in i:
        if str.isdigit(j):
            if int(j) > 100:
                cleansing_list.append(0)
            else:
                cleansing_list.append(j)
        else:
            cleansing_list.append(0)

cleansing_list = [cleansing_list[i:i+responce_num] for i in range(0,peopel_num * responce_num,responce_num)]

array=[]
average_list = []

x_ = list(map(list, zip(*cleansing_list)))

array=[]
average_list = []

array = [[int(item) for item in row] for row in x_]

count = 0
for i in range(responce_num):
    count = array[i].count(0)

    if count == peopel_num:
        print(0)
    else:
        average_list = array[i]
        average = sum(average_list) / (peopel_num - count)
        print(math.floor(average))
