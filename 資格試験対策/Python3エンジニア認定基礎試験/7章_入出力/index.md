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

