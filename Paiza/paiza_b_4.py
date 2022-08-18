i = 1
seat_list = []

seat_list + str(i) = [1, 2, 3]
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# beside = 横, vertical = 縦,
import numpy as np
# a = np.array([seat[0], seat[1]])
    # b = np.array([2, 3])
    # # マンハッタン距離を求める
    # manhattan_distance = np.linalg.norm(a - b , ord=1)



integer_list = []
manhattan = []
manhattan_seat = []

reserved_seat = []
manhattan_list = [[0, 3], [2, 1], [3, 2]]

seat_number = []
seat_list = []

integer_list = list(map(int, input().split()))
# print(integer_list) -> [9, 4, 5, 2, 3]
i = 0

for i in range(len(integer_list)):
    if i == 0:
        reserved_num = integer_list[i]
    elif i == 1:
        beside = integer_list[i]
    elif i == 2:
        vertical = integer_list[i]
    elif i == 3 or i == 4:
        manhattan.append(integer_list[i])

number = beside * vertical
count = 0

for x in range(beside):
    sublist = []
    for y in range(vertical):
        sublist.append(x, y)
     seat_list.append(sublist)
print(seat_list)
# for i in range(reserved_num):
#     seat_number = list(map(int, input().split()))
#     reserved_seat.append(seat_number)

#     for n in reserved_seat:


    # if manhattan_distance == 2:
    #     if seat == manhattan_list[0] or seat == manhattan_list[1] or seat == manhattan_list[2]:
    #         manhattan_seat.append(seat)
    #         count += 1
    #         print(manhattan_seat)
    # # elif (2 - seat_number[0]) + (3 - seat_number[1]) < 2 or (2 - seat_number[0]) + (3 - seat_number[1]) > 2:
    # #     seat_list.append(seat_number)
    # else:
    #     pass

    #     print(manhattan_seat)



# while True:
#     seat_number = list(map(int, input().split()))
#     seat_list.append(seat_number)
#     count += 1
#     if count == 20:
#         break

# for s in range(number):
#     seat_number = list(map(int,input().split()))
#     seat_list.append(seat_number)

# for y in range(vertical):
#     for x in range(beside):
#         seat_list.
#     seat_list +

# print(num, beside, vertical, manhattan) # -> 9 4 5 [2, 3]
