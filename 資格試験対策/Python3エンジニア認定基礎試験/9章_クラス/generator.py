def reverse(data):
    # game -> 4文字 - 1, (3, -1, -1)
    # index3から-1ずつ、index-1まで取得
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

reverse_word = reverse("game")
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))
print(next(reverse_word))



# for char in reverse("game"):
#     print(char)

# def word(data):
#     for s in data:
#         yield s

# for one_word in word("game"):
#     print(one_word)
