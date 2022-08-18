# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_list = []
num_list = []
i = 0

for i in range(10000):
    while len(num_list) == 16:
        num_list.append(map(int, input()))

        if num_list[i] == num_list[i+1]:
            num_list[i] = num_list[i] + num_list[i+1]
            i += 1

        else:
            i += 1



# for i in range(10000):
#     num = input()
#     num_list.append(int(num))

#     if len(num_list) == 16:
#         new_list = []
#         for x in len(num_list):
#             new_list.append(num_list[x])
#             if new_list[x] == num_list[x+1]:
#                 new_num = new_list[x] + num_list[x+1]
#                 new_list.insert(x, new_num)
#             else:
#                 continue

#     i += 1
    #     if num_list[i] == num_list[i+1]:
    #         num_list[i] = num_list[i] + num_list[i+1]
    #     elif num_list[i] !== num_list[i+1]:
    #         num_list[]



    # if len(num_list) == 16:
    #     print(num_list)
    #     break
        # while True:
        #     for s in range(len(num_list)):
        #         if num_list[s] == num_list[s+1]:
        #             num_list[s] = num_list[s] + num_list[s+1]
        #         else:
        #             continue

    # elif len(num_list) < 16:
    #     i += 1

