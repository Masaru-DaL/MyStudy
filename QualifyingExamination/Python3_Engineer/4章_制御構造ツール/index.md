# 4章_制御構造ツール
出題数 9問

## 1. if文
- もし ○○ なら ×× する

#### 1-1. もしaが1ならhelloと表示し、もしaが2ならworldと表示する

```python: if
if a == 1:
  print("hello")
if a == 2:
  print("world")
```

#### 1-2. もしaが1ならhelloと表示し、もしbが10ならPythonと表示する

```python: if
if a == 1:
  print("hello")
if b == 10:
  print("Python")
```

#### 1-3. もしaがhelloならworldと表示し、もしaがworldならhelloと表示する

```python: if
if a == "hello":
  print("world")
if a == "world":
  print("hello")
```

#### 1-4. もしaが10以下なら小さいと表示し、もしaが100以下なら中ぐらいと表示する

```python: if
if a <= 10:
  print("小さい")
if a <= 100:
  print("中ぐらい")
```

これは誤りです。
実際に実行してみましょう。

```python: if
def main():
  a = 5
  if a <= 10:
    print("小さい")
  if a <= 100:
    print("中ぐらい")

if __name__ == "__main__":
  main()
```

実行結果は
小さい
中ぐらい
と、両方が出力されています。
`a=5`が10以下でもあり、100以下でもあるからです。
10以下の時、11以上100以下の時と別に処理する必要があります。

100以下の時の処理を`elif a <= 100`か`if 10 < a and a <= 100:`に書き換える事で期待通りにプログラムが処理されます。

#### 1-5. もしaが10以下なら小さいと表示し、100以下なら中ぐらい、100より大きいなら大きいと表示する

4のコードに、
`else:`か`elif a > 100:`を追加します。
どちらも`print("大きい")`と続けます。


## 2. for文
- 繰り返しの処理をする(回数を伴う)
  - 深呼吸を**10回**する
  - 戸締りの確認を**2回**する
  - 手を**3回**洗う
  - など

#### 2-1. リスト(数字)
```python: for
def main():
  for i in [1, 2, 3]:
    print(i)

if __name__ == "__main__":
    main()
```
1
2
3

1. i = 1, print(i)
2. i = 2, print(i)
3. i = 3, print(i)
リストに格納された個数分繰り返される。

#### 2-2. リスト(文字列)
```python: for
def main():
  for i in ["Python", "R", "SQL"]:
    print(i)

if __name__ == "__main__":
    main()
```
Python
R
SQL

#### 2-3. 変数の変更、文字列の長さも表示
iをwordに変更し、print()での出力に変数word+文字列の長さを出力させる

```python: for
def main():
  for word in ["Python", "R", "SQL"]:
    print(word, len(word))

if __name__ == "__main__":
    main()
```
Python 6
R 1
SQL 3

## 3. while, break
- 条件を満たす限り、処理を繰り返す
  - 部屋がキレイになる**まで**、掃除を**続ける**
  - ラスボスを倒す**まで**、ゲームを**続ける**
  - 5kg減量できる**まで**、ダイエットを**続ける**

**条件に何を入れるかが重要**

#### 3-1. whileの条件: i < 10
変数iの初期値が0、iに1ずつ足しながら10より小さい間は繰り返す

```python: while
def main():
  i = 0
  while i < 10:
    print(i)
    i = i + 1

if __name__ == "__main__":
    main()
```
0
1
2
3
4
5
6
7
8
9

#### 3-2. whileの条件: len(moji) < 5
変数mojiの初期値はa、mojiにaを1つずつ足しながら文字列の長さが5より小さい間は繰り返す

```python: while
def main():
  moji = "a"
  while len(moji) < 5:
    print(moji)
    moji = moji + "a"

if __name__ == "__main__":
    main()
```
a
aa
aaa
aaaa

#### 3-3. break
- 繰り返し処理を中断する
  - ラスボスを倒すまで、ゲームを続ける。ただし、親に注意されたら**中断(break)**

1. 変数iが3の倍数になったら中断
(3の倍数、つまりiを3で割った余りが0ということ)

```python: break(while)
def main():
  i = 0
  while i < 10:
    print(i)
    i += 1
    if i % 3 == 0:
      break

if __name__ == "__main__":
    main()
```
0
1
2

:::message
0, 1, 2と出力して+1する度にif文で判定されるが、3の倍数でない場合はbreakの処理はされない。
iが3の倍数になってif文に判定され、3の倍数ということを満たした時にbreakの処理、つまり中断される。
:::

2. 変数iが5の倍数になったら中断
iの初期値が10
iが100より小さい時には繰り返す
iが5の倍数になったら中断する
なお、printの出力で5で割った時の数も同時に出力する

```python: break(while)
def main():
  i = 10
  while i < 100:
    print(i, i % 5)
    i += 1
    if i % 5 == 0:
      break

if __name__ == "__main__":
    main()
```
10 0
11 1
12 2
13 3
14 4


## 4. rangeとcontinue
#### 4-1. range
:::message alert
rangeは指定した数字の1個前までしか取得出来ない、という所を覚えておく必要がある。
indexが0から始まる点と合わせて意識しておくと安心。
:::

連続した数字を取得することが出来る
1. 例えば、`for i in range(5):`とすると5回繰り返す。

```python: range
def main():
  for i in range(5):
    print(i)

if __name__ == "__main__":
    main()
```
0
1
2
3
4

2. 連続した数字を取得(0~)
0から20までの数字から、5刻みで数字を取得する

```python: range
def main():
  for i in range(0, 20, 5):
    print(i)

if __name__ == "__main__":
    main()
```
0
5
10
15

3. 連続した数字を取得(not0~)
10から20までの数字から、2刻みで数字を取得する

```python: range
def main():
  for i in range(10, 20, 2):
    print(i)

if __name__ == "__main__":
    main()
```
10
12
14
16
18

3. 連続した数字を取得(-から始める)
-10から5までの数字から、3刻みで数字を取得する

```python: range
def main():
  for i in range(-10, 5, 3):
    print(i)

if __name__ == "__main__":
    main()
```
-10
-7
-4
-1
2

#### 4-2. continue
- 繰り返し処理をスキップして、次に移る

1. 変数iが3の時だけ処理をスキップする
処理を中断して以降を行わないのではなく、あくまでも条件を満たした時の処理だけをスキップする

```python: continue(range)
def main():
  for i in range(5):
    if i == 3:
      continue
    print(i)

if __name__ == "__main__":
    main()
```
0
1
2
4


## 5. for, break, else
#### 5-1. break
- 繰り返し処理を中断させる
iが5になったらfor文を中断させる
```python: break(for)
def main():
  for i in range(10):
    if i == 5:
      break
    print(i)

if __name__ == "__main__":
    main()
```
0
1
2
3
4

#### 5-2. for文終了後に実行する節else
正常に終了した場合にのみ実行されるfor文の中で使用出来るelse句
0~9まで出力され、for文が終了した後にelse句が実行される。

```python: else(for)
def main():
  for i in range(10):
    print(i)
  else:
    print("最後まで繰り返しました")

if __name__ == "__main__":
    main()
```
0
1
2
3
4
5
6
7
8
9
最後まで繰り返しました

#### 5-3. 5-2のfor文の途中でbreak
```python: break(for, else)
def main():
  for i in range(10):
    if i == 5:
      break
    print(i)
  else:
    print("最後まで繰り返しました")

if __name__ == "__main__":
    main()
```
0
1
2
3
4

最後まで処理が行われず、5になった時点で処理が中断される。
また、最後まで処理が行われていないので、else句が実行されない。


## 6. pass, def
#### 6-1. def
- 関数を定義する
- 処理に名前を付けて、再利用しやすくする
- 後で見返す時、他の人が見た時にわかりやすい関数名を書くことが重要

関数を実行すると`hello`と出力される関数名を`print_hello`と付ける。

```python: def
def print_hello():
  print("hello")

if __name__ == "__main__":
    print_hello()
```
hello

#### 6-2. pass
- 後で処理を書きたい時の仮置きに使う
何も実行されない事を利用して、一時的にエラーを起こさないように仮置きすることの使用が多い

```python: pass(def)
def do_nothing():
  pass

if __name__ == "__main__":
    do_nothing()
```
何も実行されない。


## 7. 引数, キーワード引数
#### 7-1. 引数
- 関数に情報を与える
`print_something`の引数に`something`を渡し、この引数は関数を実行する時に指定する引数となる。
実行する際の引数に`"apple"`を指定する。

```python: def
def print_something(something):
  print("hello", something)

print_something("apple")
```
hello apple

#### 7-2. 引数: 複数の引数を与える
2つの引数を足し算する

```python: def
def plus_a_b(a, b):
  print(a + b)

plus_a_b(10, 20)
```
30

#### 7-3. 引数: デフォルト値を設定
- 接尾辞を付ける
`add_suffix`の第2引数に`"xxx"`という文字列をデフォルト値として代入する
実行の引数には`"hello"`だけ指定する
`"hello"` + `suffix(デフォルト値)`

```python: def
def add_suffix(text, suffix = "xxx"):
  print(text + suffix)

add_suffix("hello")
```
helloxxx

#### 7-4. キーワード引数
- 引数に与える時に名前を付ける
関数の第2引数にデフォルト値が代入されている
実行する時に、第2引数に新たに値を指定する事でデフォルト値を更新する

```python: def
def add_suffix(text, suffix = "xxx"):
  print(text + suffix)

add_suffix("hello", suffix = "yyy")
```
helloyyy

`suffix = "yyy"`と名前を付けて関数を呼び出す事を**キーワード引数**と呼ぶ。

#### 7-5. 位置引数
引数の値だけ指定して関数を呼び出す。
`[関数名]("hello")`の`"hello"`が位置引数

:::messege
位置引数とキーワード引数の違いは、関数を実行する時の引数の渡し方。
位置引数は引数の値だけ書く。
キーワード引数はhoge=fugaのように書く。
:::

#### 7-6. 可変の引数を与える
`*args`がタプル、`**kwargs`が辞書型として受け取る

1. 関数を定義する

```python: def
def kansu(a, *args, **kwargs):
  print(a, type(a))
  print(args, type(args))
  print(kwargs, type(kwargs))
```

2. 第一引数の`a`を確認する
第一引数に値を渡す

`kansu(1)`
1 <class 'int'>
() <class 'tuple'>
{} <class 'dict'>
`a`に1が入り、int型である事が分かる。
タプルと辞書型には何も入らない。

`kansu("a")`
a <class 'str'>
() <class 'tuple'>
{} <class 'dict'>
`a`にaが入り、文字列型である事が分かる。
タプルと辞書型には何も入らない。

3. 複数の引数を指定する(tuple)
`kansu(1, 2, 3, 4)`
1 <class 'int'>
(2, 3, 4) <class 'tuple'>
{} <class 'dict'>
`a`に1が入り、2, 3, 4はタプルとなる。
辞書型には何も入らない。

a <class 'str'>
('b', 'c', 'd') <class 'tuple'>
{} <class 'dict'>
`a`に文字列aが入り、b, c, dはタプルとなる。
辞書型には何も入らない。

4. 複数の引数を指定する(dict)
`kansu(1, x="x", y="y", z="z")`
1 <class 'int'>
() <class 'tuple'>
{'x': 'x', 'y': 'y', 'z': 'z'} <class 'dict'>
`a`に1が入り、x, y, z = x, y, zがそれぞれ辞書型として入る。
タプルには何も入らない。

`kansu(1, x=10, y=20, z=30)`
1 <class 'int'>
() <class 'tuple'>
{'x': 10, 'y': 20, 'z': 30} <class 'dict'>
`a`に1が入り、x, y, z = 10, 20, 30がそれぞれ辞書型として入る。
タプルには何も入らない。

5. それぞれを組み合わせる
`kansu(1, 2, 3, 4, x=10, y=20, z=30,)`
1 <class 'int'>
(2, 3, 4) <class 'tuple'>
{'x': 10, 'y': 20, 'z': 30} <class 'dict'>
`a`には1が入り、2, 3, 4がタプル、x, y, z = 10, 20, 30が辞書型として入る。

:::message alert
ちなみに、
`kansu(1, x=10, y=20, z=30, 2, 3, 4)`
このように引数を渡すとエラーが起こる。
> positional argument follows keyword argument
> 位置指定引数はキーワード引数に続くという意味
位置引数とキーワード引数を合わせて使用する場合、**キーワード引数の後に位置引数を書けない**というルールになっている為に起こる。
:::


## 8. lambda(ラムダ)式
#### 8-1. lamdba式とは
- 無名関数(名前のない関数)を定義する

```python: def
def plus_one(x):
  return x + 1

print(plus_one(10))
```
11

```python: lambda
plus_one = lambda x: x+1

print(plus_one(10))
```
11

**上記2つは同じ意味(結果)**

#### 8-2. lambda式の使い所-1
- リストの各要素を2乗する

```python: lambda
a = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, a))

print(square)
```

1. lambda式で引数を指定して2乗したい場合
`square = lambda x: x**2`
`sqiare(10)`
100

2. map関数とは
引数の順番に注意する。
`map(関数, シーケンス)`と指定するのがmap関数の使用上のルール
つまり、加工元となる値群を第二引数に指定し、それをどのように加工するのかというところが第一引数によって指定させることとなる。

3. list関数とは
```python: list
def square(x):
  result = x ** 2
  return result

a = [1, 2, 3, 4, 5]

result = map(square, a)
```
2乗する関数を第一引数に、2乗したいリスト`a`を第二引数に指定しています。
これを出力します。

`print(result)`
とすると、mapオブジェクトと返ってきてしまう。
リストの各要素に関数を適用させるので、結果はリストとして出力させる必要があるため、
`print(list(result))`
と出力すると、
[1, 4, 9, 16, 25] と無事出力出来ました。

4. map関数とlambda式を組み合わせる
def関数を用いても結果は同じ結果を出力出来るが、lambda式を用いるとコードがもっとすっきりする。

- なぜlambda式を使うのか？いつ使うの？
:::message
> lambda式は、**単体で使うのではなく、他の関数と組み合わせて使う事を前提とした関数の定義文**である。
これは無形関数と呼ばれる事から分かるように、lambda関数を使う事で構文がより簡潔になることと関係があります。
また、1文字目のアルファベット順ではなく、2文字目のアルファベット順に並べたいといった少し複雑な処理を関数やメソッドを用いて実行したい場合に真価を発揮するようです。

sort, max, map, filterなどの関数・メソッドと共に用いる事が多いので、これらを見かけたらlambda式の活用を考えてみると良い
:::

#### 8-3. lambda式の使い所-2
- キーを指定してソートする
2番目の要素順に並び替える。

```python: sort
b = [[1,2], [2,1], [0,3]]
b.sort(key = lambda x: x[1])

print(b)
```
[[2, 1], [1, 2], [0, 3]]

`b.sort(key = lambda x: x[1])`
でkeyのindex番号を1(2番目)に指定出来ます。

`b.sort(key = lambda x: x[0])`
[[0, 3], [1, 2], [2, 1]]
もちろん、keyを0(1番目)に指定すれば先頭の要素順にソート出来ます。

#### 8-3. lambda式の使い所-3
- 条件に合致する要素を抽出する
リスト`a`から3より大きい要素を抜き出す。

```python: filter
a = [1, 2, 3, 4, 5]
match = list(filter(lambda x: x>3, a))

print(match)
```
[4, 5]

:::message
filter関数とは
> filter(f1, iterable) 関数は、第二引数に渡したコレクション (iterable) オブジェクトの要素を、 第一引数の関数 f1 にひとつずつ渡して評価し、True となる要素だけからなるコレクションを作成します。
:::


## 9. docstring
#### 9-1. docstringとは？
- ドキュメントをコード内に残す記法
- 未来の自分や、同僚のための情報になる
- 書き方
  - ダブルクオーテーションを3つ書き、その中にコメントを記述する
  - 書き方にいくつかの流派がある

#### 9-2. Google流docstring
1. VScodeで簡単に利用するための拡張機能を入れる。
`autoDocstring: VSCode Python Docstring Generator`
をインストールする。

2. pythonファイル内でダブルクオーテーションを3つ書くと、`Generate Docstring`という候補が出るのでエンターを押すと補完する事が出来る。

```python: docstring(google)
"""_summary_

  Args:
      x (_type_): _description_

  Returns:
      _type_: _description_
  """
```

- summary section
  - 説明のタイトル

- Args section
  - 引数の名前、型、optional(省略可能)かどうかなど、引数の説明を記載するセクション

- Returns section
  - return文を使用した関数の戻り値を記載するセクション

:::message
補完で出てくるのは上の3つだが、Googleスタイルでは以下の用途別に定義されたセクションがある。
Attributes、 Args、Returns、Yields、Raises、Examples、Note、Todo
:::


## 10. 関数アノテーション
#### 10-1. 関数アノテーションとは
**関数注釈**とも呼ばれる。
任意で使うことが出来るオプションで、引数や戻り値に入るべき型を記述できる。

```python: Annotations
def plus_one(x: int) -> int:
  return x + 1
```

```python: Comments
def plus_one(x: "x is int") -> int:
  return x + 1
```

:::message
実装の参考にはなるが、挙動の変化はない。
型以外にもコメントを書く事が出来る。
:::

#### 10-2. 型を確認してみる。
`関数名.__annotations__` で型を確認出来る。

```python: annotations
def plus_one(x: int) -> int:
  return x + 1

print(plus_one(1))
print(plus_one.__annotations__)
```
2
{'x': <class 'int'>, 'return': <class 'int'>}

引数xがint, 戻り値もintとなっている事が確認出来ます。

#### 10-3. コメントの方も確認してみる

```python: comments
def plus_one(x: "x is int") -> int:
  return x + 1

print(plus_one(1))
print(plus_one.__annotations__)
```
2
{'x': 'x is int', 'return': <class 'int'>}


## 11. PEP8
#### 11-1. PEPとは
- Python Enhancement Proposal(パイソン エンハンスメント プロポーサル)
- Python機能拡張提案
- Pythonに関する機能を議論した結果がまとめられている資料のこと

#### 11-2. PEP8
- Pythonのコーディング規約が書かれている
  - コードは書くよりも読まれる方が多い
  - 読みやすいコードを書くためのノウハウが書かれている

#### 11-3. コーディング規約の例
- インデントはスペース4つ
- コロンやセミコロンは直前にスペース不要
- i = i + 1のようにイコールの前後はスペースを入れる
- など

#### 11-4. black
- PEP8を全て覚えるのは手間
- 自動で読みやすくしたい
- コードレビューでの指摘は高コスト

**規約が非常に多い**ことから上記の問題がある。
そこで、blackというソフトウェアを用いると、**コーディング規約に沿うように自動で変換**してくれる。

#### 11-5. blackの設定(VScode)
[Pythonの自動フォーマッター「black」を入れようとしたら苦戦した話](https://zenn.dev/masaruxstudy/articles/6ebe32ed5490e0)
