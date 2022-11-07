class TestClass:
    morning = "Good Morning!!" # クラス変数
    def greeting(self):
        print(self.morning)

instance1 = TestClass()        # インスタンス1
instance1.greeting()

instance2 = TestClass()        # インスタンス2
instance2.greeting()

# 実行結果: Good Morning!!
# 実行結果: Good Morning!!
