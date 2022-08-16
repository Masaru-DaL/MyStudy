# 10章_標準ライブラリめぐり
出題数 4問

## 1. 標準ライブラリ Part.1
#### 1-1. OSとやりとりをする
- OSをやりとりをするには`OS`というライブラリを用いる

```python: os
# OSというライブラリをインポートする
import os

# カレントディレクトリを返す
os.getcwd()

# カレントディレクトリを変更
# 現在のディレクトリ内にsampleディレクトリを作成後
os.chdir("./sample")

# ディレクトリを作成するコマンドの実行
# 上でディレクトリを変更しているのでsampleディレクトリ内にsample2ディレクトリが作成される
os.system(('mkdir sample2'))
```
1. 現在のディレクトリが絶対パスで出力される。
2. **相対パス**で指定したsampleディレクトリに移動
3. sampleディレクトリ内にsample2ディレクトリを作成

:::message
各コマンドの意味
`getcwd` -> get current working directory
`chdir` -> change directory
`mkdir` -> make directory
:::

#### 1-2. ファイルやディレクトリの管理
- `shutil`(シューティル)というライブラリを用いる
:::message
[YAHOO! 知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10248221400)
shutil -> `SHell UTILities`の略
utilitiesは便利なツール(群)といった意味。
**≠ shellを操作するユーティリティ**
よくshellを使って行われる操作を行うモジュールなのでこういう名前になってるようです。
:::

```python: shutil
import shutil

# ファイルをコピー
# カレントディレクトリにsample1.txtを作成後
shutil.copyfile('sample1.txt', 'sample2.txt')

# ファイルを移動
# コピーして作成したsample2.txtをカレントディレクトリにあるsampleディレクトリに移動させる
shutil.move('sample2.txt', './sample/sample.txt')
```
sampleディレクトリ内にsample2.txtがあればOKです。

#### 1-3. ファイルの検索
- `glob`というライブラリを用いる
:::message
glob -> 英語で「かたまり」という意味
globを用いることで特定のパターンにマッチするファイルを取得することができる。

`*`(ワイルドカード)を用いて使用することが多いように、特定のファイルの「かたまり」を取得する、というイメージで良いと思われる。
:::

```python: glob
import glob

# globディレクトリの「.txt」ファイルを探す
# 相対パスでpathを指定する
files = glob.glob('./glob/*.txt')
print(files)
```
['./glob/sample1.txt', './glob/sample2.txt', './glob/sample3.txt']

#### 1-4. コマンドライン引数の取得
下記のファイルを`get.py`として作成する
```python: argv
import sys

if __name__ == "__main__":
    print(sys.argv)
```
ターミナルで
`python get.py one two three`
を実行する。

['get.py', 'one', 'two', 'three']

- 実行結果から分かること
1. `sys.argv`はリスト。
2. 文字列として格納される。
数値として扱いたい場合には`int()`, `float()`で変換が必要。
3. 1つ目の要素にスクリプトファイルのパスが格納される。
フルパスやファイル名のみかはOSによって異なる。

:::message
`python get.py one two three`
で行っている事というのは、`get.py`に、one, two, threeを渡しています。
この渡した値(コマンドライン引数)を用いてどうするか、というのを`sys.argv`で設定することが出来る。
:::

