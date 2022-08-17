# 模擬試験を行う
[PRIME STUDY](https://study.prime-strategy.co.jp/)
こちらでPython3エンジニア認定基礎 模擬試験が無料で行えます。
模擬試験を通して間違った所やポイントなどを更に学習していきます。

## Pythonの特徴(誤りはどれか)
> Pythonでは、文のグルーピングはカッコで囲うことでなくインデントで行われるなど、プログラムを小さく読みやすく書けるという特徴がある。ただ変数や引数の宣言は必要である。

これは「変数や引数の宣言は必要」という記述が間違っています。
宣言 -> 型宣言のことです。
他言語では変数に値を代入する前に、`int i;`のように変数の型宣言が必要になります。
Pythonでは型宣言をすることなく変数に値を代入することが可能です。

## formatメソッドの理解が必要
- formatメソッド
`置換フィールドを含む文字列.format(値1, 値2, ...)`
`"名前{0}です。{1}歳。住所は{2}です。".format("Yamada", 18, "Tokyo")`
0番目、1番目とformat(1, 2)が紐づいています。

```python:
a = 10
b = a ** 2          # b = 100
c = b % 20 + 5      # c = 5
d = 8
e = d / b           # e = 0.08
f = d // c          # f = 1(// -> 切り捨て除算)

print ('{0}, {1}'.format(e, f))
```
{0} -> 0.08(e)
{1} -> 1(f)

## 実行結果がエラーになるコード
```python:
Zen = 'SimpleIsBetterThanComplex'
Zen[0] = 'J'
```
出来そうに思えたのですが、`TypeError: 'str' object does not support item assignment`となります。
文字列の理解が不足していました。

**文字列は不変である(変更出来ない)**
- 変更するにはどうしたらいいか
1. 完全に書き直す
2. リストに変換する

## range(a, b, c)の挙動
以下のコードで出力されるもの
```python:
for i in range(-10, -30, -5):
    print(i, end=",")
```
-10,-15,-20,-25
(-10,-15,-20,-25,-30 -> X)
:::message
`range(a, b, c)` ->
`a=start`, `b=stop`, `c=step`

`start <= i < stop`、もしくは`start >= i > stop`という挙動になるので、stop値を含まない点に注意する必要があります。
:::


## enumerate()
`enumerate()`を使うと、forループの中でリストやタプルなどのいてらぶるオブジェクトの要素と同時にインデックス番号(カウント、順番)を取得できる。

```python: for
name_list = ['Alice', 'Bob', 'Charlie']

# 通常のfor文
for name in name_list:
    print(name)
```
Alice
Bob
Charlie

```python: enumerate
name_list = ['Alice', 'Bob', 'Charlie']

# enumerateを使用したfor文
for i, name in enumerate(name_list):
    print(i, name)
```
0 Alice
1 Bob
2 Charlie

- 問題内容
```md:
次の結果を得たい場合、コードの2行目以降を代替するものとして正しいものはどれか。なお各選択肢の次の行には「 print(i, v) 」が記述されるものとする。

[ 実行結果 ]
0 Now
1 is
2 better
3 than
4 never

[コード]
Zen = ['Now','is','better','than','never']
for i in range(len(Zen)):
    print(i, Zen[i])
```

実行結果が、index番号, 要素となっていることから、
これと同じ動作をさせたい場合は`enumerate()`を利用すれば良いことが分かる。


## 関数の中の変数
- 問題
```md:
次のコードの実行結果として正しいものはどれか。

i = 5
i = 6

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()
```
出力結果 -> 6

```python:
def f(arg = i):
    i = 7
    print(arg)

f() # 実行後、エラーになる。
-----------------------------
def f(arg = i):
    i = 7
    print(arg)

i = 6

f() # 実行後、エラーになる。
-----------------------------
i = 6

def f(arg = i):
    i = 7
    print(arg)

f() # 実行後、6が出力される。
```
上の結果から分かるように、ここで定義された関数は直前の変数`i`を引数として実行される事が分かりました。

:::message alert
関数の外と中で同じ名前の変数を使用しても、それぞれが独立した変数として扱われる。
:::

:::message
関数の中と外で同じ変数にアクセスする方法
1. オブジェクトを介してメンバ変数としてアクセスする
2. グローバル変数として宣言する
3. グローバル変数として宣言したあと、モジュール化する
:::


## 関数の出力
```md:
次のコードに関し、【A】の行の出力として正しいものはどれか。

[コード]
def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4)) 【A】
print(culc(4, 5))
```
([1], [1])
([1, 4], [1, 27])
([1, 4, 9], [1, 27, 64])
([1, 4, 9, 16], [1, 27, 64, 125])

実行結果から分かるように、実行する度にそれぞれの空のリストに`append`で追加されていくのが分かります。
関数で定義した空のリストの宣言が、関数の外で宣言した場合と同じ動作をすることが確認できたので、理解を深められました。

```python:
squares=[]
cubes=[]

def culc(a, b=1):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4))
print(culc(4, 5))
```
([1], [1])
([1, 4], [1, 27])
([1, 4, 9], [1, 27, 64])
([1, 4, 9, 16], [1, 27, 64, 125])
