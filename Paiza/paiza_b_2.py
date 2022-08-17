# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num_people, num_count = input().split()
num_people = int(num_people)
num_count = int(num_count)

point_list = [''] * num_people


for i in range(num_count):
    point_list[i] = list(map(int, input().split()))

print(point_list[0])
print(point_list[1])
print(point_list[2])
