import itertools

word_list = []

num = input()
num = int(num)

for i in range(num):
    word = input()
    word_list.append(word)

for pair in itertools.combinations(word_list, 2):
    num = 0
    for name in pair:
        pairname = ''.join(name)
        print(pairname)
        # print(pairname)
        # if pairname in word_list:
        #     if True:
        #         for i in word_list:
        #             if len(pairname) <= len(i):
        #                 num += 1
        #     else:
        #         continue

# print(num)
