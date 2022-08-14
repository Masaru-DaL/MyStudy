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

