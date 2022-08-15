# エラーと例外

出題数 4 問

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

for の前に「式」が必要(例えば i, i+1 など)

#### 1-3. 例外: exception-1

- 実行中に検知されたエラー
  `print(10 / 0)`

```c:error
    print(10 / 0)
ZeroDivisionError: division by zero
```

0 で割り算は出来ない為

#### 1-4. 例外: exception-2

- 未定義の変数を呼ぼうとした時のエラー
  `sushi + "wasabi"`

```c: error
    sushi+"wasabi"
NameError: name 'sushi' is not defined
```

**NameError**
sushi が定義されていませんよ、と出る

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

int + str の順にすると以下のエラーが起こる

```c: error
    1 + "1"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

ちょっと難しいので引用させて頂くと、

> +という計算の記号(演算子)は、int 型と str 型の間の計算には使えません、というような意味です。
> 言っている事は int と str は計算出来ませんよ、ということです。

#### 1-6. 例外に出会った場合

**解決方法を学ぶ**

- 最終行のエラーメッセージをググる
- 自分独自のコードに関する箇所は消して、ググる
- 例外が発生する最小のコードを作って再現させて、質問する

#### 1-7. 例外が発生した場合の処理を予め記述しておくことが出来る

1. `try ~`
2. `except ~`
   try の中で例外が起きたら、except へ処理を移す。
   どんな例外かで分岐が可能
   書き方は`if`, `elif`, `else` と良く似ています。

#### 1-8. TypeError を処理した例

`"1" + 1`を実行すると、
`TypeError: can only concatenate str (not "int") to str`
TypeError が返ってきます

```python: try, except
try:
  "1" + 1
except TypeError:       # TypeErrorの時
  print("TypeErrorです")
except:                 # TypeError以外の時
  print("何かのエラーが起きています")
```

TypeError です

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
`try, except`が TypeError にしか対応させていないため、それ以外となります。

#### 1-10. try 内のコードは最小限に抑える

- 意図しない箇所での例外処理を防ぐ必要がある
  - `else`が利用出来る
  - try 内のコードが正常に処理された場合、else 内が処理される

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

print("try, else 文の実行")
例外処理に引っかからず、無事に処理を行えました。

## 2. 例外創出とユーザー定義例外

#### 2-1. 例外の送出

- 好きなタイミングで例外を発生させることが出来る
  ` raise 例外名("メッセージ")`

```python: raise
raise NameError("Hi There")
```

    raise NameError("Hi There")

NameError: Hi There

```python: raise
try:
    raise NameError("Hi There")
except NameError as e:
    print(e)
```

Hi There

:::message
下の方が分かりやすいかもしれません。
try 節で raise を使用し、NameError クラスの例外を発生させています。
try 節で例外が発生したので、except 節の処理が実行され、エラーメッセージが表示されています。
:::

#### 2-2. Exception: 何かの例外

- NameError などは Exception の派生
  Exception は例外の基底クラスなので、書き方は同じで良い。

```python: Exception
# raise Exception("何らかの例外")

try:
    raise Exception("何らかの例外")
except Exception as E:
    print(E)
```

何らかの例外

#### 2-3. 自分でエラーを出して、例外処理をする練習

上記では`try` -> `except` の流れに移る処理の流れを見るだけでしたので、try, except を使ってエラーを出してみます。

```python: error
try:
  raise NameError("Hi There")
except NameError:
  print("NameErrorが出た")
  raise
```

NameError が出た
...
raise NameError("Hi There")
NameError: Hi There

:::message
最後の`raise`がないと except の処理に移り、同じように print しか実行しないので、最後に`raise`を実行し、エラーを送出します。
:::

#### 2-4. ユーザー定義例外

- 自作の例外で、関数ないで起きた問題を明確にする
  - try ~, except ~ で例外処理が可能
  - 通常の関数と同じように記述可能
  - 名前の最後に Error を付ける慣習
  - 複雑な処理はさせずに、エラー理由が分かると良い

#### 2-5. 自作の例外(1 例)

MyError というクラスを作成する

```python: MyError
class MyError(Exception):
    pass


def main():
    try:
        raise MyError("マイエラー")
    except MyError as e:
        print("Error Massage: ", e)
        raise


if __name__ == "__main__":
    main()
```

Error Massage: マイエラー
...
raise MyError("マイエラー")
**main**.MyError: マイエラー

## 3. 例外処理 クリーンアップ動作の定義

#### 3-1. クリーンアップ動作の定義

- try から抜け出す時に必ず実行される
- try 内で例外が発生しても実行される
  - `finally`という処理で書く事が出来る

```python: cleanup
try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, world!!")
```

Goodbye, world!!
...
raise KeyboardInterrupt
KeyboardInterrupt

#### 3-2. finally とは

- try が正常終了した場合も実行される

```python: cleanup
try:
    print("try内の実行")
finally:
    print("Goodbye, world!!")
```

try 内の実行
Goodbye, world!!

#### 3-3. 例外処理における役割分担

:::message

- try
  - 例外が発生するかもしれない処理
- except
  - 例外発生時の対応方法
- ele
  - try 正常終了時の処理
- finally
  - 何が起きても実行される
    :::

#### 3-4. 実装例

- 上記全てを使用する
- `divide` -> 割り算を処理

- 各役割
  :::message
- try
  - `x / y`の時に例外が発生するかもしれない
- except
  - `x / y`が 0 で除算された時に行う対応
- else
  - `x / y`が 0 除算されず、正常に処理が行われた場合に行う処理
- finally
  - 何が起きても実行する処理
    :::

上記の処理を行うコード

```python: divide
def divide(x, y):
  try:
    result=x/y
  except ZeroDivisionError as ZDE:
    print(" 0除算されました ")
  else:
    print(" 答えは ", result)
  finally:
    print("finally 実行中 ")
```


