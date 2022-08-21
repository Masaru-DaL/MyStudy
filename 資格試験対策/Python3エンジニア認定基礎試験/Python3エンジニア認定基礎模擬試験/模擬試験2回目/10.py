for n in range(2, 10):
    # print(n)
    for x in range(2, n):
        # print(n, x)
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            continue
    else:
        print(n, "is a prime number")

# for i in range(2, 3):
#     print(i)

######################################
# coding: utf-8

# for文で、breakしない
# for x in range(3):
#     print(x)
# else:
#     print('else')

# for文で、breakする
# for x in range(3):
#     if x == 2:
#         break
#     print(x)
# else:
#     print('else')

# for文で、breakする
# for x in range(3):
#     if x == 3:
#         break
#     print(x)
# else:
#     print('else')
