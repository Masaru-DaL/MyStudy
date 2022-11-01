class TestClass:
    # コンストラクタ
    def __init__(self):
        # 引数greetingの値をインスタンス変数の初期値とする
        print("Hello World!!")

    def wave_hands(self):
        print("手を振る")

    def walk(self):
        print("歩く")

instance1 = TestClass() # インスタンス化
# ここで実行するとコンストラクタの"Hello World!!"のみが出力する
#instance1.wave_hands()  # instance1が手を振るようになる
#instance1.walk()        # instance1がさらに歩くようになる
