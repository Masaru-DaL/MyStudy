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
