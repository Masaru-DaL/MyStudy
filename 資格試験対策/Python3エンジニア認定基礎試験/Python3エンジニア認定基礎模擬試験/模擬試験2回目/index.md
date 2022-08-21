## Pythonの特徴
 Pythonは柔軟な配列や集合、ディクショナリといった、非常に高水準のデータ型を組み込みで持つ。データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、Perlと比べると同程度である。

**データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、Perlと比べると同程度である。**が間違い。

データ型の一般性が高いためPythonの対応可能な問題領域は**Awkよりもずっと広く**、**Perlと比べてさえ広く**、その上たいていのことは他の言語と同程度以上に簡単に出来る。


## 変数に対しての指定
- 問題
```md:
次の変数Zenに関して指定した場合、実行時にエラーとならないものはどれか。

Zen = 'BeautifulIsBetterThanUgly'
```

- 回答を間違った答え
  - `Zen[10] = 'a'`

一見出来そうではあるが、文字列は不変であるため、indexを指定して新しい値を入れることは出来ないため、エラーが起こる。
`TypeError: 'str' object does not support item assignment`

- 正答
  - `Zen[1000:10000]`

#### スライスの理解を深める
`>>> Zen = 'BeautifulIsBetterThanUgly'`

`>>> Zen[0:4]` # index[0] ~ index[3]
'Beau'

`>>> Zen[:4]` # 左を省略した場合 [0:4] という指定になる
'Beau'

`>>> Zen[4:]` # 右を省略した場合 [4:最後まで]という指定になる
'tifulIsBetterThanUgly'

`>>> Zen[4:-1]` # この場合は index[4] ~ index[-1]の1個手前までとなる
'tifulIsBetterThanUgl'

`>>> Zem[:]` # 左右を省略した場合は全てを指定している
'BeautifulIsBetterThanUgly'

##### オーバーした数を指定した場合
`>>> Zen[1000:]` # スタートの数がないので何も出力されない
''

`>>> Zen[:1000]` # 0~最後までという指定になる
'BeautifulIsBetterThanUgly'

`>>> Zen[1000:1000]` # スタートの数がオーバーしている
''

- 正答
  - `Zen[1000:10000]`

これは何も出力されないが、エラーとはならないという所を覚えておく必要がある。


## for文　continue, break, else
- 問題
```md:
次の結果を得たい場合、コード【A】【B】に入る組み合わせとして適切なものはどれか。なお【A】は★aの行と、【B】は★bの行と同じ数の空白でインデントされている。

[ 実行結果 ]
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

[ コード ]
for n in range(2, 10):
            for x in range(2 ,n): 　　…★b
                      if n % x == 0:
                                print(n, 'equals', x, '*', n//x) …★a
                                【A】
            【B】
                      print(n,'is a prime number')
```

- continue
```python: continue
# coding: utf-8

# xが3の時continueする
for x in range(5):
    if x == 3:
        continue
    print(x)
```
実行結果 -> 0 1 2 4
このように、`if x == 3:`の条件に合う時だけ、それ以降の処理を行わず、ループ文の最初に戻ります。

- break
```python: break
# coding: utf-8

# xが3の時breakする
for x in range(5):
    if x == 3:
        break
    print(x)
```
実行結果 -> 0 1 2
このように、`if x == 3:`の条件に合った時、ループ自体が終了します。

- else
```python: else
# coding: utf-8

# for文で、breakしない
for x in range(3):
    print(x)
else:
    print('else')
```
実行結果 -> 0 1 2 else
**【B】は選択肢からもelseということが分かる。**

```python: else(break)
# coding: utf-8

# for文で、breakする
for x in range(3):
    if x == 2:
        break
    print(x)
else:
    print('else')
```
実行結果 -> 0 1

```python: else(break)
# for文で、breakする
for x in range(3):
    if x == 3:
        break
    print(x)
else:
    print('else')
```
実行結果 -> 0 1 2 else (`if x == 3`の条件は満たされていない)

- for, elseの組み合わせの場合、ループ文の処理の後にelseが実行されます。
- for+break, elseの組み合わせの場合、breakを使用しなかった時だけelseが実行されます。

#### 最初の問題に戻る
```md:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            【A】
    【B】
        print(n, "is a prime number")
```

- n, xがどうなっているか
```pyhon:
for n in range(2, 10):
    print(n)
    for x in range(2, n):
        print(n, x)
```
2 (range(2, 2)の時はxは出力されない)
3
3 2
4
4 2
4 3
5
5 2
5 3
5 4
6
6 2
6 3
6 4
6 5
7
7 2
7 3
7 4
7 5
7 6
8
8 2
8 3
8 4
8 5
8 6
8 7
9
9 2
9 3
9 4
9 5
9 6
9 7
9 8


- 一部を切り取って考える
6
6 2
6 3
6 4
6 5


#### continue
`6 % 2` -> `print(n, "equals", x, "*", n // x)`
引き続きループ文が実行される。

`6 % 3` -> `print(n, "equals", x, "*", n // x)`
`6 % 4`の判定 -> 該当しない
`6 % 5`の判定 -> 該当しない

elseの実行
`print(n, "is a prime number")`

- 実行結果
6 equals 2 * 3
6 equals 3 * 2
6 is a prime number

#### break
`6 % 2` -> `print(n, "equals", x, "*", n // x)`
これが実行された時点でループから抜ける。

- 実行結果
`6 equals 2 * 3`


この事から、【A】に当てはまるのが**break**ということが分かる。


## Pythonの可変長引数(*args, **kqargs)
- 問題
```md:
次のコード1行目の【A】【B】に入る組み合わせとして正しいものはどれか。

[ コード ]
def shop(name,【A】, 【B】):
    print("flowershop:", name)
    keys = sorted(argsX.keys())
    for kw in keys:
        print(kw, ":", argsX[kw])
    for Y in argsY:
        print(Y)

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")
```

ここで選択に出てくる`*~`と、`**~`が分からなかったので理解していきます。
- `*args`
  - 複数の引数をタプルとして受け取る
- `**kqargs`
  - 複数のキーワード引数を辞書として受け取る


- `*args`, `**kwargs`というのは慣例として使われる事が多い。
   - `*`と`**`が頭についていれば他の名前でも問題ない(モジュール名などではないという事)

#### *args
```python: *args
def my_sum(*args):
    return sum(args)

print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3, 4))
```
1
3
10

このように、関数の引数に`*`をつけて定義すると、任意の数の引数を指定する事が出来る。

#### **kqargs
```python: **kwargs
def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)

func_kwargs(key1=1,)
func_kwargs(key1=1, two=2)
```
kwargs:  {'key1': 1}
kwargs:  {'key1': 1, 'two': 2}

このように、関数の引数に`**`をつけて定義すると、任意の数のキーワード引数を指定する事が出来る。

更に細かく理解したい人: [Pythonの可変長引数（*args, **kwargs）の使い方](https://note.nkmk.me/python-args-kwargs-usage/)

#### 問題を解く
`shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")`

1. `"Iris`がまず`name`引数に入る。
2. 続いて複数の引数を指定している。
   1. `"Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed."`
3. その後に続けてキーワード引数を指定している。
   1. `bouquet="Sunflower",plants="Pachira",dried="Rose"`

この事から、
`def shop(name,【A】, 【B】):`は、
`def shop(name, *args, **kwargs)`と言う事が分かる。


## 関数に関して
#### docstring
- 1行目はいつでも常に、オブジェクトの目的の短く簡潔な要約とすべきである。
- 更に続きがある場合は、**2行目を空行**とし、**要約と他の記述を視覚的に分離すべき**である。

#### アノテーション
アノテーション -> 注釈のこと

- 引数のアノテーション
`def 関数名(引数1: int, 引数2: str):`
このように引数の後ろに:(コロン)をつけて、アノテーションの内容を記載する。

- 戻り値のアノテーション
`def 関数名(引数1, 引数2) -> int:`


- 問題
`例えば「def func(a: int, b:str) -> value」と関数を記述したときにアノテーションに該当するものは「-> value」のみである。`

これは間違いで、
`-> value`, `:int`, `:str`がアノテーションに該当します。


## zip()
- 問題
```md:
次の実行結果を得たい場合に、コードの2行目（★印の行）を代替するものとして正しいものはどれか。

[実行結果]
[(1, 4, 8), (3, 9, 27), (5, 25, 125)]

[コード]
matrix = [[1, 3, 5], [4, 9, 25], [8, 27, 125]]
power = [[row[i] for row in matrix] for i in range(3)] ★
print(power)
```

- Point
  - 2次元リスト -> リスト + タプル(中の要素)へ変換しているということ。

#### タプルからリストへ変換する
```python: list -> tuple
# リストからタプルへ変換する
language_list = ['Python', 'Java', 'C#']
print(language_list)

language_tuple = tuple(language_list)
print(language_tuple)
```
['Python', 'Java', 'C#']
('Python', 'Java', 'C#')
期待した結果になっています。

```python: list -> tuble
# 2次元リストからタプルへ変換する
language_list = [['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl']]
print(language_list)

language_tuple = tuple(language_list)
print(language_tuple)
```
[['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl']]
(['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl'])
期待した結果ではなく、タプルの中にリストがある状態になっています。

#### zip関数を使う
zip関数は、2つ以上あるリスト型や辞書型、タプル型などの要素を変換出来ます。

```python: zip
# 2次元リストからタプルへ変換する
language_list = [['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl']]
print(language_list)

language_tuple = list(zip(language_list))
print(language_tuple)
```
[(['Python', 'Java', 'C#'],), (['C', 'PHP', 'Ruby'],), (['Go', 'Dart', 'Perl'],)]
期待した通りに出力されません。

`language_tuple = list(zip(language_list))`を`language_tuple = list(zip(*language_list))`に変えると期待した通りに出力されます。
[('Python', 'C', 'Go'), ('Java', 'PHP', 'Dart'), ('C#', 'Ruby', 'Perl')]

変更点は、zipの引数に`*`を付ける点です。

- リスト自体に`*`を付けた時の処理を確認する
```python: *list
language_list = [['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl']]
print(language_list)
print(*language_list)
```
[['Python', 'Java', 'C#'], ['C', 'PHP', 'Ruby'], ['Go', 'Dart', 'Perl']]
['Python', 'Java', 'C#'] ['C', 'PHP', 'Ruby'] ['Go', 'Dart', 'Perl']
この時点で出力されている内容が違う事が分かります。

`print(*language_list)`の出力は、
`print(language_list[0], language_list[1], language_list[2])`と同じ出力である事が分かります。
よって、`*list名`とする事で、リストの内容を別個に取り出して関数に渡しているということが分かりました。

なので、`power = list(zip(matrix))`ではなく、`power = list(zip(*matrix))`が正答ということになります。


## リスト内包表記
- 問題
```md:
次の実行結果を得たい場合に、コード1行目～5行目を代替するものとして正しいものはどれか。

[ 実行結果 ]
[(1, 3), (1, 2), (1, 5), (2, 3), (2, 5), (3, 2), (3, 5)]

[ コード ]
combs = [] # ...①
for x in [1,2,3]: # ... ③
    for y in [3,2,5]: # ...④
        if x != y: # ... ⑤
            combs.append((x, y)) # (x, y) # ... ②

print(combs)
```
結果は以下の通り
[① ② ③ ④ ⑤]
① -> combs = []
② -> combs.append((x, y))
③ -> for x in [1,2,3]
④ -> for y in [3,2,5]
⑤ -> if x != y
combos = [(x, y) for x in [1,2,3] for y in [3, 2, 5] if x != y]

#### 二重ループ処理のリスト内包表記を理解する
1. ①でリストの作成を行なっています。

2. 最初のfor文`for x in [1,2,3]`で、`[1, 2, 3]`から1つ要素を取り出します(③)
   1. 最初の要素は`1`

3. 次のfor文`for y in [3,2,5]`で、`[3,2,5]`から要素を順番に取り出します(④)
   1. `3 -> 2 -> 5`の順番で取り出します

4. 次にif文`if x != y`を行います。
   1. `if 1 != 3` -> `if 1 != 2` -> `if 1 != 5`の順番です。
   2. `!=`は左右が等しくないという意味なので、xが1の時に`(x, y)`に追加されるのは、`(1, 3)`, `(1, 2)`, `(1, 5)`です。


- 一番左に書かれるのは`式`(繰り返しなどをおこなった後、どうするかという事を記述します。)

**[式 for 変数 in イテラブルオブジェクト]**


## モジュールの検索パス
- モジュールがインポートされる時の検索順序
1. **ビルドインモジュール**の中にこの名前のモジュールがないか検索する。
2. 1で見つからなければ、`sys.path`変数で得られるディレクトリのリストを使って`モジュール名.py`を検索する

:::message
シンボリックリンクを置いてあるディレクトリは、モジュールの検索パスに入らない。
:::

- `sys.path`が初期化されている場所
  - 入力スクリプトのあるディレクトリ(ファイル名が指定されてないときはカレントディレクトリ)
  - PYTHONPATH(ディレクトリ名のリスト。構文はシェル変数PATH Hと同じ)
  - インストールごとのデフォルト


## formatメソッドの理解
- 問題
```md:
次のコードの実行結果として正しいものはどれか。

import math
print('{1:.5f}, {0:.3f}'.format(math.pi, math.e))
```
`{1:.5f}`, `{0:.3f}`
この、`:.5f`というのは小数点第何位まで表示するかという意味。
`1:`というのは整数何桁だと思い込んでいました。
ただしくは、**数値を指定すると何番目の引数を当て込むか**というものです。

```python: format
print("名前{0:}です。{1:}歳。".format("Honda", 32))
print("名前{1:}です。{0:}歳。".format("Honda", 32))
```
名前Hondaです。32歳。
名前32です。Honda歳。

`format(引数1番目, 引数2番目)`が`{数値:}`の番号と連動しています。



