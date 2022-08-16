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
- Bad Point

- Good Point
- Bad Point
