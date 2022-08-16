# OSというライブラリをインポートする
import os

# カレントディレクトリを返す
print(os.getcwd())

# カレントディレクトリを変更
# 現在のディレクトリ内にsampleディレクトリを作成後
os.chdir("./sample")

# ディレクトリを作成するコマンドの実行
# 上でディレクトリを変更しているのでsampleディレクトリ内にsample2ディレクトリが作成される
os.system(('mkdir sample2'))
