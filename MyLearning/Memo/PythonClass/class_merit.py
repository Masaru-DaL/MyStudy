# man1 = "Bob"
# man1_japanese = 60
# man1_english = 90
# man1_average = (man1_japanese + man1_english) / 2

# female1 = "Lisa"
# female1_japanese = 100
# female1_english = 70
# female1_average = (female1_japanese + female1_english) / 2

# print(man1, "の平均点は", man1_average, "です。")
# print(female1, "の平均点は", female1_average, "です。")

# 平均点を出す関数
# def average(name, japanese, english):
#     average_point = (japanese + english) / 2
#     print(name, "の平均点は", average_point, "です。")

# average("Bob", 60, 90)
# average("Lisa", 100, 70)

# ①クラスを定義する
class Average():
    # ②クラス内に処理を実装する
    def __init__(self):
        self.name = ""
        self.japanese = 0
        self.english = 0
        self.average = 0

    def average_call(self):
        self.average = (self.japanese + self.english) / 2

# ③man1, female1という変数にクラスを実装する
man1 = Average()
female1 = Average()

# ④man1, female1に中身を実装していく
man1.name = "Bob"
man1.japanese = 60
man1.english = 90
female1.name = "Lisa"
female1.japanese = 100
female1.english = 70

# ⑤平均を出す関数を実行してそれぞれの平均点を出す
man1.average_call()
female1.average_call()

# ⑥実行結果
print(man1.name, "の平均点は", man1.average, "です。")
print(female1.name, "の平均点は", female1.average, "です。")
