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

# man1 = "Bob"
# female1 = "Lisa"

# average(man1, 60, 90)
# average(female1, 100, 70)

# クラスを定義する
class Average():
    # クラス内に関数を定義します
    def average(self, man1, female1, japanese, english):
        average_point = (japanese + english) / 2
        self.man1 = "Bob"
        self. female1 = "Lisa"
        print(man1, "の平均点は", average_point, "です。")
        print(female1, "の平均点は", average_point, "です。")

man1 = Average() # 変数man1にAverageクラスを実装する
man1.average(60, 90)

female1 = Average()
female1.average(100, 70)
