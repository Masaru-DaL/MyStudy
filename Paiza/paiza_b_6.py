### 入力される値
## 1回目の入力
# A -> 地図のサイズ, (A*A) A通り、Aマス
# B -> 降水量を表す整数, B以上で通る事ができない
## 2回目以降の入力
# num1 num2 num3 *A回入力される

## 制約条件
# 他のルートに移動することは出来ない
# 自宅待機で良い場合 -> wait と出力
# 行く事が出来る場合
# -> 通る事ができるルートの番号を出力(route1 route2 route3)

# coding: utf-8

size_num, rain_percent = map(int, input().split())
# print(size_num, rain_percent) #

route_list = []
after_route_list = []
result_list = []

count = 0
for i in range(size_num):
    route_list = list(map(int, input().split()))
    after_route_list.append(route_list)

if after_route_list[0][0] >= rain_percent or after_route_list[1][0] >= rain_percent or after_route_list[2][0] >= rain_percent:
    if after_route_list[0][1] >= rain_percent or after_route_list[1][1] >= rain_percent or after_route_list[2][1] >= rain_percent:
        if after_route_list[0][2] >= rain_percent or after_route_list[1][2] >= rain_percent or after_route_list[2][2] >= rain_percent:
            print("wait")

else:
    result_list.append(1)

if after_route_list[0][1] >= rain_percent or after_route_list[1][1] >= rain_percent or after_route_list[2][1] >= rain_percent:
    pass
else:
    result_list.append(2)

if after_route_list[0][2] >= rain_percent or after_route_list[1][2] >= rain_percent or after_route_list[2][2] >= rain_percent:
    pass
else:
    result_list.append(3)

    print(*result_list)
