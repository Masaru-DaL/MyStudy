class Reverse:
    # 引数にdata(整数)を渡すと、文字数を計算する
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    # 文字数が0なら例外処理
    # 文字をindex-1(逆)から返す
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


reverse = Reverse("spam")
for char in reverse:
    print(char)
