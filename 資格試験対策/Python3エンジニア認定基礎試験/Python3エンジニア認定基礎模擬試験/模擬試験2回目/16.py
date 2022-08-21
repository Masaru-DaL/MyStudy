def shop(name, *argsY, **argsX):
    print("flowershop:", name)
    keys = sorted(argsX.keys())
    for kw in keys:
        print(kw, ":", argsX[kw])
    for Y in argsY:
        print(Y)

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")


# def my_sum(*args):
#     return sum(args)

# print(my_sum(1))
# print(my_sum(1, 2))
# print(my_sum(1, 2, 3, 4))


# def func_kwargs(**kwargs):
#     print('kwargs: ', kwargs)

# func_kwargs(key1=1,)
# func_kwargs(key1=1, two=2)
