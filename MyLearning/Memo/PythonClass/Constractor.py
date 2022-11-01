class TestClass:
    greeting = "Hello World!!" # 初期値: Hello World!!
    def __init__(self):
        self.year = 2022
        self.greeting = "Hello Constructor!!"

instance = TestClass()

print(instance.year)
print(instance.greeting)

# 出力結果: 2022
# 出力結果: Hello Constructor!!
