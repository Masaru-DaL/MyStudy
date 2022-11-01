class TestClass:
    # test_method1: 引数messageの値を表示する
    def test_method1(self, message):
        print(message)

    # test_method2: test_method1を呼び出す
    def test_method2(self):
        self.test_method1("Hello self!!")

# インスタンス化
instance = TestClass()

# メソッドの呼び出し
instance.test_method2()

# 出力 -> Hello self!!
