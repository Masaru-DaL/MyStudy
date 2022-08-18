# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num_people, num_count = input().split()
num_people = int(num_people)
num_count = int(num_count)

point_list = [''] * num_people
max_point_list = []

for i in range(num_count):
    point_list[i] = list(map(int, input().split()))
    max_point_list.append(max(point_list[i]))

if max_point_list.count(max(max_point_list)) == 1:
    print(max_point_list.index(max(max_point_list)))
elif max_point_list.count(max(max_point_list)) >= 2:
    for i in range(num_count):
        point_list[i].remove(max(point_list[i]))
        print(point_list[i])







# print(max_point_list.count(max(max_point_list)))
# print(max(max_point_list))
