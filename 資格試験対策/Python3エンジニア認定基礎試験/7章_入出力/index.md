# 7章_入出力
出題数 1問

## 1. 入出力 1/2
#### 1-1. str()
`str(object)`
- objectを**人間が読みやすい文字列**に変換して返す。
  - エンドユーザーに出力する

```python: str
word = "Hello, world"
print(str(word))
```
Hello, world

#### 1-2. repr()
`repr(object)`
- objectを`eval()`で**再び元のオブジェクトに戻せる文字列**に変換して返す。
- representationの略
  - デバッグ用に出力する
※`eval`は第一引数を式として評価する

```python: repr
word = "Hello, world"
print(repr(word))
```
'Hello, world'

#### 1-3. str.rjust()
- 右揃えを行う
- 引数は、左側のスペースを含む文字列

```python: rjust
word = "Hello, world"
print(word.rjust(20))
print(word.rjust(30))
```
        Hello, world
                  Hello, world

#### 1-4. str.ljust()
- 左揃えを行う
- 引数は、右側のスペースを含む文字列

```python: ljust
word = "Hello, world"
print(word.ljust(20))
print(word.ljust(30))
```
'Hello, world        '
'Hello, world               '
(本来はクオートは付かないが、空白が見えるように付けています。)

#### 1-5. str.center()
- 中央揃えを行う
- 引数はスペース含む全体の文字数
```python: center
word = "Hello, world"
print(word.center(20))
print(word.center(30))
```
'    Hello, world    '
'         Hello, world         '
(本来はクオートは付かないが、空白が見えるように付けています。)

#### 1-6. str.zfill()
- 0で埋めて最低文字数を揃える
- 引数で指定した数に文字列が足りてない場合のみ0で埋められ、指定した数以上に出力された場合は意味がない

```python: zfill
print("123".zfill(5))
print("3.14".zfill(5))

# num1にint型で値を代入する
# num1をstrに変換してからzfillを適用する
num1 = 10.2
print(str(num1).zfill(8))

num2 = "3.1415926535"
print(num2.zfill(5)) # 効果無し
```
00123
03.14
000010.2
3.1415926535

#### 1-7. str.format()
- 文字列に変数を代入する

1. 通常の使い方
```python: format
print("Hello, {}".format("Misaki"))

# 変数自体を変数を代入できる形にする
word2 = "Hello, {}"
print(word2.format("Taro"))
```
Hello, Misaki
Hello, Taro

2. 代入先に名前を付けることも出来る
こちらの方が可読性が上がる

```python: format(name)
print("Hello, {name}".format(name="Misaki"))

word2 = "Hello, {name}"
print(word2.format(name="Taro"))
```
Hello, Misaki
Hello, Taro

3. 小数点第何位まで表示するか
```python: format{}
import math

# Pi == π
# 小数点第2位まで表示する
print("Pi is about {0:.2f}".format(math.pi))

# 何桁分のスペースを確保するか
print("{0:10d}".format(12345))
```
Pi is about 3.14
     12345

#### 1-8. formatをもう少し理解する
- 小数点第1位まで表示
`{:.1f}`

- 小数点第3位まで表示
`{:.3f}`

- 文字の表示位置を指定する(引数に20をした場合)
  - `{:<20}`：左寄せ
  - `{:^20}`：中央寄せ
  - `{:>20}`：右寄せ

- 桁数指定(0で埋める)
`a = 1234567890`
`print('{:020}'.format(a))`
00000000001234567890

- 桁区切りを指定する(3桁ごとのみ)
`a = 1234567890`
`print('{:,}'.format(a))`
1,234,567,890

他の詳しい所の参考サイト: [Pythonの文字列フォーマット（formatメソッドの使い方）](https://gammasoft.jp/blog/python-string-format/)

#### 1-9. f文字列: Python3.6からの新機能
- 古い参考書に掲載されていない可能性あり
- 変数を自動で参照してくれる

```python: f
name = "Taro"
print(f"Hello, {name}")
```
Hello, Taro


## 2. 入出力 2/2
#### 2-1. open(read)
- ファイルを開く(読み込みモード)
- 書き方
  - `open(開くファイル, mode)`
第2引数のmodeは、
1. 読み出し専用なら `r`
2. 書き込み専用なら `w`
3. ファイルを追記用に開くなら `a`
:::message
mode引数は省略可能で、省略された場合には`r`であると仮定されます
:::

#### 2-2. read()
- `open`で開いたファイルを読み込む
open -> read のコードを記述する

```python: open, read
# 変数にはファイルの格納場所のパスを指定出来る(絶対パス or 相対パス)
path = './str.py'
file1 = open(path)
print(file1.read())

# カレントディレクトリの場合はこちらの書き方でOK
file2 = open('str.py')
print(file2.read())
```
word = "Hello, world"
print(str(word))

word = "Hello, world"
print(str(word))
(出力されるものは同じ)

#### 2-3. open(write)
- 新規ファイルを書き込みモードで開く
- または、既存ファイルを書き込みモードで開く

#### 2-4. write()
- 新規ファイルの場合は新しく書き込む
- 既存ファイルの場合は上書きする

```python: write
# ファイル自体も新規作成される
file1 = open("new.py", "w")
file1.write("Hello, Python")
file1.closed

# ファイルが上書きされる
file2 = open("str.py", "w")
file2.write("Hello, Python")
file2.closed
```
`-> cat new.py`
`Hello, Python`

`-> cat str.py`
`Hello, Python`
str.pyには元々以下が記述されていた
`word = "Hello, world"`
`print(str(word))`
