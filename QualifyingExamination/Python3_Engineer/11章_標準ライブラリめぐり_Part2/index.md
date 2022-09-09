# 11章 標準ライブラリめぐり Part.2
出題数 1問

## 1. 標準ライブラリめぐり Part.5(10章の続き)
#### 1-1. 学ぶライブラリを限定
- 11章では非常に多くのライブラリが紹介されており、全部を覚えるのは困難(+出題数が1問)
- また、その多くは特定の用途でしか使わないものが多い

- 11章で紹介されているライブラリの紹介 / その中でも使われるであろうライブラリ、今回学ぶものは**太字**
  - reprlib
  - pprint
  - textwrap
  - locale
  - string
  - struct
  - **threading**
  - **logging**
  - weakref
  - array
  - **collections**
  - **bisect**
  - **heapq**
  - **decimal**

#### 1-2.　マルチスレッド: threading
**リソースを効率的に使うプログラムを書ける**

- Good Point
  - 複数のCPUをフルに使う
  - ファイルの入出力待ち時間を有効利用
- Bad Point
  - バグが混入しやすくなる
  - プログラムの可読性が落ちやすい

#### 1-3. ログ取り: logging
**問題が発生した時の証拠を残す**

- Good Point
  - バグの原因が見つけやすい
  - ログは標準エラー出力。標準出力と分離が可能
- Bad Point
  - 適切なログを残すのが難しい
  - 大きなループ内でログを出すと大量のログを生み、ログファイルが大きくなる

#### 1-4. collectionモジュールのdeque
**両端のリストへのアクセスを高速化**

- Good Point
  - 左端へのappendやpopより高速
  - 右端へのアクセスも高速的
  - 通常のリストと同様に使う事が出来るので扱いやすい
- Bad Point
  - 両端以外のアクセスが遅い

```python: deque
from collections import deque

d = deque(["task1", "task2"])
print(d)

# 右端へ追加
d.append("task3")
print(d)

# 左端へ追加
d.appendleft("task4")
print(d)
```
deque(['task1', 'task2'])
deque(['task1', 'task2', 'task3'])
deque(['task4', 'task1', 'task2', 'task3'])

#### 1-5.　ソート済みのリストへの処理: bisect
**ソートを毎回実行する必要がなくなる**

- Good Point
  - 短いコードで書く事が出来る
- Bad Point
  - ソート済みの必要がある
  - 知らない人が多い

```python: bisect
import bisect

# ソートしている場合
scores1 = [1, 2, 4]
bisect.insort(scores1, 3)
print(scores1)

# ソートしていない場合
scores2 = [12, 11, 14]
bisect.insort(scores2, 13)
print(scores2)

# 一度ソートする
scores3 = [12, 11, 14]
scores3.sort()
bisect.insort(scores3, 13)
print(scores3)
```
[1, 2, 3, 4]
[12, 11, 13, 14]
[11, 12, 13, 14]

:::message
`bisect.insort(a, x)`
1. `bisect_right()`を実行して挿入箇所を特定する
2. `a`に対して`insert()`メソッドを実行する
3. ソート順を維持するために適切な位置に`x`を挿入する
:::

#### 1-6. ヒープ: heapq
**最小値が常に位置ゼロに入る**
特定の条件下で有効。汎用的ではない。

- Good Point
  - 完全なソートが不要
  - 最小値へのアクセスが高速
- Bad Point
  - 効率面からソートの代替にならない

#### 1-7. 10進数の浮動小数点計算
**手計算と一致させる事が出来る**

- Good Point
  - 2進数の浮動小数点による計算誤差がなくなる
  - 丸め規則を厳密に守る事が出来る
:::message
丸め規則とは、四捨五入などによって発生する実際の値との誤差を最小限にするための丸めをどうするか、というのを定めたもの
:::

```python: decimal
from decimal import Decimal

print(0.70 * 1.05)

# round(式, 丸める桁数)
# roundでの四捨五入では誤差が発生する
print(round(0.70 * 1.05, 2))

# decimalを用いて丸め規則に則って結果を出力する
print(round(Decimal("0.70") * Decimal("1.05"), 2))
```
0.735
0.73
0.74
