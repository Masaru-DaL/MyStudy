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


## 引数の指定
- 問題
```md:
次の関数を呼び出す際に、引数の指定として正しいものはどれか。

def location(city, state, country='Japan'):
    print("I live in",country,".")
    print("My company is located in",city,",",state,".")
```
- 間違った指定
location(state='California', country='USA', 'San Francisco')
`SyntaxError: positional argument follows keyword argument`のエラーになります。
引数の指定に問題があるという文法エラーで、「**位置引数がキーワード引数に続いている**」という意味です。

:::message alert
キーワード引数の後に位置引数を書けない！
というルールを覚えておかなくてはいけません。
:::

正しい引数の指定は、
location('San Francisco', state='California', country='USA') となります。

正当としては`location(state='Tokyo', city='chiyoda')`でした。
:::message
この引数の指定方法は、デフォルト引数が設定されているから可能です。デフォルト引数が設定されていない場合は、countryが指定されなくなるので、エラーになります。
:::


## Pythonでより良い事
- 間違った解答
演算子の周囲やカンマの後ろ、カッコの内側にもスペースを入れ読みやすさに配慮すべきである。
**カッコの内側にもスペースを入れ**が間違いですかね。

- main関数に引数を指定して実行する時の書き方
  - main(10)    ...Good
  - main( 10 )  ...Bad

良く考えれば分かったかも...。

- 正答
国際的な環境で使用する予定のコードでは、PythonのデフォルトであるUTF-8か、さらにプレーンなASCIIが常に最良である。
ASCIIは違うな、と思ったのですが、PEP8で記載されているようでした。
**国際的な環境で使用する予定のコード**という所を注目して覚えておきます。


## pop()の動作確認
- 引数を指定した場合
`pop(1)` -> index1を取り出す

- 引数を指定しなかった場合
`pop()` -> 末尾(index-1)を取り出す


## Bool値
`print((1, 2, 3, 4) > (1, 2, 5))`
-> False

- (1, 2, 3, 4) > (1, 2, 5)
1. 左のタプルのindex1と右のタプルのindex1 -> 左のindex2, 右のindex2 ...の順番で比較されていく。
   1. 1 > 1 -> False
この時点でFalseとなる。

- 試してみる
`>>> (1) > (1)`
False
`>>> (2) > (1)`
True

最初の時点でFalseとなったが、比較する順序は、
**左右のタプルのindex番号同士を順番に比較する。**

### 文字列の比較
文字列を比較する場合の判断基準は、**文字の順番**で決まる。
もっと詳しく言うと、**文字のUnicodeコードポイント(文字コード)**で判定される。

`'PHP' < 'Perl' < 'Python'`
-> True
これを試してみる。

- Unicodeコードポイントの調べ方
  - 組み込み関数`ord()`で取得可能
  - 1文字ずつしか出来ない

```c:
>>> ord('a')
97
>>> ord('z')
122
>>> ord('A')
65
>>> ord('Z')
90
```
- 上記から分かること
  - 小文字 > 大文字
  - 小文字(97~122)
  - 大文字(65~90)

ポイント数を出して調べるのが確実ではあるが、時間的にも労力的にも大変。

`'PHP' < 'Perl' < 'Python'`
小文字の数だけで比較して、
0 < 3 < 5
これだけで比較出来ます。


## math
mathモジュールで使用出来る関数`pi`と`e`を理解する。

```python: math(pi, e)
import math

print(math.pi)
print(math.e)
```
3.141592653589793
2.718281828459045

- math.pi
  - 3.14~から分かるように円周率です。

- math.e
  - 2.718...
  - 自然対数の底(ネイピア数)
  - [【ネイピア数】とは わかりやすくまとめてみた【自然対数の底(e)】](https://coinbaby8.com/napiers-number.html)

:::message
math.piは円周率(3.14...)と覚えておきます。
math.eは2.718...なんだなぐらいの理解でとどめておきます。
(機械学習、統計学を学ぶならある程度知っておいた方が内容のようです。)
:::


## エラーと例外から
パーサ（構文解釈器）は違反のある行を表示し、最後にエラーが検知された点を小さな矢印で示す。エラーは矢印より後のトークンが原因である。

上記は一見正そうに見えるが、`エラーは矢印より後のトークンが原因である。`が間違いです。
正しくは`エラーは矢印より**前**のトークンが原因である。`

```python: error
>>> while True print('hello world')
  File "<stdin>", line 1
    while True print('hello world')
               ^^^^^ # これが小さな矢印
SyntaxError: invalid syntax
```

`while True`の後に`:`がないため、エラーになっています。
`>>> while True: print('hello world')`
と打ち込むとセカンダリプロンプトが表示されます。(エラーは起きません。)


## 例外処理
- 問題
```md:
次の実行結果を得たい場合、コードの【A】【B】に入る組み合わせとして適切なものはどれか。

[ 実行結果 ]
Saya is a
intelligent
speedster.

[コード]
class OurException(Exception):
    pass
def raise_her_exception(a):
    print(a, 'is a')
    raise 【A】
    print('easygoing person.')
def func(key: int):
    try:
        if key == 0:
            raise_her_exception('Saya')
    except OurException as e:
        print('intelligent')
        raise 【B】

key = 0
try:
    func(key)
except Exception as f:
    print('speedster.')
```

- raiseとは？
  - 意図的に例外を発生させる。

- 処理の流れを追う
```python:
## 実行結果
# Saya is a
# intelligent
# speedster.

class OurException(Exception):
    pass
def raise_her_exception(a):
    print(a, 'is a')                    # ...③
    raise #【A】
    print('easygoing person.')
def func(key: int):
    try:
        if key == 0:
            raise_her_exception('Saya') # ...②
    except OurException as e:
        print('intelligent')            # ...④
        raise #【B】

key = 0
try:
    func(key)                           # ...①
except Exception as f:
    print('speedster.')                 # ...⑤
```
1. `func(key)`の実行
   1. funcの引数は0で実行する

2. `key == 0`が条件に当てはまるので、`raise_her_exception('Saya')`が実行される。
   1. raiseraise_her_exception関数の引数にSayaを指定して実行
   2. `Saya is a`が出力される

3. 次の出力、`intelligent`を出力したい
   1. `print('intelligent')`は`OurException`(もしくは`e`)という例外処理が実行された時。
   2. `raise【A】`で発生させる例外は`OurException`という事が分かる。

4. `OurException`の実行
   1. `intelligent`が出力される。

5. 最後に`speedster.`を出力したい。
   1. `print('speedster.')`は`Exception`という例外が発生した時。
   2. `raise【B】`で発生させるのは`Exception`という事が分かる。

正答: 【A】OurException　【B】Exception


## クラス
- クラスオブジェクトは2種類の操作をサポートする。
1. 属性参照
   1. [0. Python の基本的な注意点](http://www-mete.kugi.kyoto-u.ac.jp/zaki/db/lec0.html)
   2. `object.name`の形式で行われる

2. インスタンス化
   1. `MyClass`が定義済みとした時、`instanceA = MyClass()`でMyClassの新しいインスタンスが生成され、`instanceA`に代入されます。

- 問題
  - クラスに__init__()メソッドが定義してあると、新規生成されたインスタンスに対して自動的に__init__()メソッドがコールされる。ただし__init__()メソッドに引数を与えることはできない。

この説明は間違いです。
`__init__()メソッドに引数を与えることはできない`という点が間違いです。
`__init__()`には引数を与える事ができ、設定しておくことでクラスのインスタンス化を行う時に与える引数となる。
(もちろん、__init__メソッドに引数を与える場合、引数を処理する記述は必要)


## コマンドライン引数
- 問題
```md:
コマンドライン上で「python3 script.py one two three four five」を実行したときに、以下の結果を得たい。コード2行目の【A】に入るものとして正しいものはどれか。

[ 実行結果 ]
['one', 'two', 'three']

[ コード ]
import sys
print(【A】)
```
- コマンドライン引数の処理
  - **インタープリタがスクリプト名(スクリプトのファイル名)と続く引数群を知らせると、これらは文字列のリストとなり、sysモジュールの変数`argv`に割り当てられる。**
  - `import sys`を実行することで、このリストにアクセスできる。

`python3 script.py one two three four five`を読み解く。
1. script.py
   1. これはスクリプト名なので、コードのファイル名が`script.py`というファイル名ということ。

2. `one two three four five`を参照するには
   1. `print(sys.argv)`を実行してみる
   2. `['script.py', 'one', 'two', 'three', 'four', 'five']`が出力される。

3. 実行結果である、`['one', 'two', 'three']`を出力するには
   1. リストで出力されるので、`sys.argv`のindex1~3を出力すれば良いことが分かる。
   2. スライスで[1:4]でOK(index1~4の1個手前まで)

`print(sys.argv[1:4])` -> `['one', 'two', 'three']`

:::message
1. sysモジュールをインポートすること
2. argv(sys.argv)に引数群が割り当てられること
:::


## 正規表現
- 問題
```md:
次の正規表現を用いたコードの【A】の部分に入れたときエラーとなるものはどれか。

import re
prog = re.compile('(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
【A】
print(ret[0])
```

- import re
  - 正規表現を操作するための`re`モジュール

- re.compile
  - [変数名] = re.compile(正規表現パターン文字列)
    - [変数名] -> 変数に代入され、生成されたオブジェクト
        -  正規表現に当てはまる文字列を検索するmatchメソッド
        -  文字列を置換するsubメソッド
        -  などを持ち、繰り返し使える

- re.IGNORECASE
  - 大文字、小文字の区別を行わなくなる
```python: re.IGNORECASE
# a-zの小文字全て、A-Zの大文字全て
pattern = re.compile(r'[a-zA-Z]')

# a-z(A-Z)でもOK
pattern = re.compile(r'[a-z]', re.IGNORECASE)

# A-Z(a-z)でもOK
pattern = re.compile(r'[A-Z]', re.IGNORECASE)
```

後は、`(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?'` これを読み解きます。

- (K|S)
  - KかS(小文字でも可)のどちらでもいいよ
  - 1文字の入力に対して判定されるので、どちらかに一致した時点でもう片方は無視される

- ?
  - 直前の正規表現に0回か1回繰り返したものにマッチさせる結果の正規表現にする

1. `ret = prog.search('SUSANOO')` の場合
   1. `SUSANOO` は `(K|S)us(a|u)n(a|o)(o|m)`で検索出来たのでエラーにはなりません。

2. `ret = prog.search('Kusaneiro')` の場合
   1. `Kusane`と検索していくと、`(K|S)us(a|u)n(a|o)`の時点で一致しません。
   2. `e`と`(a|o)`の部分でエラーとなります。

正答: ret = prog.search('Kusaneiro')


## 仮想環境とパッケージ
pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定はできない。

**削除対象となるパッケージの複数指定はできない。**という記述が間違い。
`pip uninstall パッケージ名`のパッケージ名は複数選択が可能


## ヒストリの保存場所
デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。

**デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。**という記述が間違い。
正しくは、`.python_history`というファイルに保存される。


