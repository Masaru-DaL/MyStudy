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

instance1.wave_hands()  # instance1が手を振るようになる
# この時点で実行すると"Hello World!!"と"手を振る"が出力される

instance1.walk()        # instance1がさらに歩くようになる
# 最終的に"Hello World!!"、"手を振る"、"歩く"が出力される
