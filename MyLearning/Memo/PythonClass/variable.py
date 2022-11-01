class TestClass:
    # コンストラクタ
    def __init__(self, greeting):
        self.greeting = greeting

instance1 = TestClass("Hello!!")
print(instance1.greeting)

instance2 = TestClass("Good Evening!!")
print(instance2.greeting)

# 実行結果: Hello!!
# 実行結果: Good Evening!!
