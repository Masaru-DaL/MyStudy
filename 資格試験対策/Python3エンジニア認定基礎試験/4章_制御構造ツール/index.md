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


`kansu("a")`
a <class 'str'>
() <class 'tuple'>
{} <class 'dict'>
`a`にaが入り、文字列型である事が分かる。

3. 複数の引数を指定する(tuple)
`kansu(1, 2, 3, 4)`
1 <class 'int'>
(2, 3, 4) <class 'tuple'>
{} <class 'dict'>
`a`に1が入り、2, 3, 4はタプルとなる。

a <class 'str'>
('b', 'c', 'd') <class 'tuple'>
{} <class 'dict'>
`a`に文字列aが入り、b, c, dはタプルとなる。

4.
