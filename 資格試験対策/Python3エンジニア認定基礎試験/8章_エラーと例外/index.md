# エラーと例外
出題数 4問

## 1. 例外と例外処理
#### 1-1. SyntaxError: invalid syntax
- 構文エラー
  - プログラムの文法が間違ってると表示される
  - エラー箇所の修正が必要

`for i in range(10)`
```c: error
    for i in range(10)
                      ^
SyntaxError: expected ':'
```
range(10)の直後にコロンが必要

#### 1-2. リスト内包表記の間違い
`[for i in range(10)]`
```c: error
    [for i in range(10)]
     ^^^
SyntaxError: invalid syntax
```
forの前に「式」が必要(例えばi, i+1など)

#### 1-3. 例外: exception-1
- 実行中に検知されたエラー
`print(10 / 0)`

```c:error
    print(10 / 0)
ZeroDivisionError: division by zero
```
0で割り算は出来ない為

#### 1-4. 例外: exception-2
- 未定義の変数を呼ぼうとした時のエラー
`sushi + "wasabi"`

```c: error
    sushi+"wasabi"
NameError: name 'sushi' is not defined
```
**NameError**
sushiが定義されていませんよ、と出る

#### 1-5. 例外: exception-3
- 文字列と数値を足そうとした時のエラー
- int と str は足し算出来ない為
`"1" + 1`

```c: error
    "1" + 1
TypeError: can only concatenate str (not "int") to str
```
**TypeError**
式の最初を文字列に指定しているので、文字列は文字列としか連結出来ません、と出る

int + strの順にすると以下のエラーが起こる
```c: error
    1 + "1"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
ちょっと難しいので引用させて頂くと、
> +という計算の記号(演算子)は、int型とstr型の間の計算には使えません、というような意味です。
言っている事はintとstrは計算出来ませんよ、ということです。

#### 1-6. 例外に出会った場合
**解決方法を学ぶ**
- 最終行のエラーメッセージをググる
- 自分独自のコードに関する箇所は消して、ググる
- 例外が発生する最小のコードを作って再現させて、質問する

#### 1-7. 例外が発生した場合の処理を予め記述しておくことが出来る
1. `try ~`
2. `except ~`
tryの中で例外が起きたら、exceptへ処理を移す。
どんな例外かで分岐が可能
書き方は`if`, `elif`, `else` と良く似ています。

#### 1-8. TypeErrorを処理した例
`"1" + 1`を実行すると、
`TypeError: can only concatenate str (not "int") to str`
TypeErrorが返ってきます

```python: try, except
try:
  "1" + 1
except TypeError:       # TypeErrorの時
  print("TypeErrorです")
except:                 # TypeError以外の時
  print("何かのエラーが起きています")
```
TypeErrorです

#### 1-9. 準備した例外以外が起きた場合
1-8 で使用したコードを用いて、`sushi + "wasabi"`(NameError)を実行してみます。

```python: try, except
try:
    sushi + "wasabi"
except TypeError:
    print("TypeErrorです")
except:
    print("何かのエラーが起きています")
```
何かのエラーが起きています
`try, except`がTypeErrorにしか対応させていないため、それ以外となります。

#### 1-10. try内のコードは最小限に抑える
- 意図しない箇所での例外処理を防ぐ必要がある
  - `else`が利用出来る
  - try内のコードが正常に処理された場合、else内が処理される

```python:try.py
print("try, else文の実行")
```

```python: try, else
try:
    file = open("try.py")
except IOError:
    print("cannot open")
else:
    print(file.read())
    file.close()
```
print("try, else文の実行")
例外処理に引っかからず、無事に処理を行えました。
