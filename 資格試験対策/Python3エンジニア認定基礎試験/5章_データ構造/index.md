# 5章_データ構造
出題数 7問

## 1. リストの加工
#### 1-1. append()
- リストに値を追加する

```python: append
list_num = [1, 2, 3]

list_num.append(4)
print(list_num)

list_num.append(5)
print(list_num)
```
[1, 2, 3, 4]
[1, 2, 3, 4, 5]

#### 1-2. extend()
- リストにリストを追加する

```python: extend
list_num = [1, 2, 3]

list_num.extend([4, 5])
print(list_num)
```
[1, 2, 3, 4, 5]

`extend(6)`としてもリストではないのでエラーになります。

#### 1-3. insert()
- indexとobjectを引数に指定し、リストに追加する

```python: insert
list_num = [1, 2, 3]

list_num.insert(0, 10) # index0に10を追加
print(list_num)

list_num.insert(3, 20) # index3に20を追加
print(list_num)
```
[10, 1, 2, 3]
[10, 1, 2, 20, 3]

#### 1-4. remove()
- 値を削除する

```python: remove
list_num = [1, 2, 3, 3, 4]

list_num.remove(1) # リストから1を削除
print(list_num)

list_num.remove(3) # indexの若い方から3を削除
print(list_num)

list_num.remove(3) # 2番目に若い方から3を削除
print(list_num)
```
[2, 3, 3, 4]
[2, 3, 4]
[2, 4]

#### 1-5. pop()
- 先頭の要素からデータを取り出して削除する
First In First Out

```python: pop
list_num = [1, 2, 3, 4, 5]

list_num.pop(0) # index0のデータを取り出す
print(list_num)

list_num.pop(3) # [2, 3, 4, 5]から、index3のデータを取り出す
print(list_num)
```
[2, 3, 4, 5]
[2, 3, 4]

#### 1-6. clear()
- リストの値そのものを削除する
- 引数を指定出来ない

```python: clear
list_num = [1, 2, 3]

list_num.clear()
print(list_num)
```
[]

引数を指定出来ないので`clear(1)`などの指定はエラーになる。

#### 1-7. index()
- 引数に値を指定するとindex番号が分かる

```python: index
list_num = [1, 2, 3, 4, 5]

print(list_num.index(1))
print(list_num.index(4))
```
0
3

#### 1-8. count()
- 引数で指定した要素がリストに何個あるか数える

```python: count
list_num = [1, 1, 2, 3, 3, 3]
print(list_num.count(1))
print(list_num.count(3))
```
2
3

#### 1-9. sort()
- リストの先頭から順に数字の若い方から、アルファベット順に並べ替える

```python: sort
list_num = [4, 8, 1, 3, 1, 2, 3, 5, 3, 3]
list_num.sort()
print(list_num)
```
[1, 1, 2, 3, 3, 3, 3, 4, 5, 8]

#### 1-10. reverse()
`list.reverse()`、もしくは`sort(reverse=True)`で、並べ替えを逆にする。

1. パターン1
```python: reverse
list_num2 = [5, 4, 3, 2, 1]
list_num2.reverse()
print(list_num2)
```
[1, 2, 3, 4, 5]
こちらは問題なく逆順に並んでいます。

2. パターン2
```python: reverse
list_num = [4, 8, 1, 3, 1, 2, 3, 5, 3, 3]
list_num.reverse()
print(list_num)
```
[3, 3, 5, 3, 2, 1, 3, 1, 8, 4]
上手く並び替えられていません。
この場合は一度ソートしてからでないと上手く並び替えが行われません。

```python: reverse
list_num = [4, 8, 1, 3, 1, 2, 3, 5, 3, 3]
list_num.sort()
print(list_num)
list_num.reverse()
print(list_num)
```
[1, 1, 2, 3, 3, 3, 3, 4, 5, 8]
[8, 5, 4, 3, 3, 3, 3, 2, 1, 1]
一度ソートしてから、逆に並び替えがきちんと行われています。

3. パターン3
`sort(reverse=True)`を使うと一度ソートする必要なく並び替えを行う事が出来ます。

```python: sort(reverse=True)
list_num = [4, 8, 1, 3, 1, 2, 3, 5, 3, 3]
list_num.sort(reverse=True)
print(list_num)
```
[8, 5, 4, 3, 3, 3, 3, 2, 1, 1]

#### 1-10. copy()
- リストをコピーする

```python: copy
list_a = [1, 2, 3]
list_b = list_a.copy()
print(list_b)
```
[1, 2, 3]

※`copy()`を使わないで同じ値を変数に定義した場合

```python: not copy
list_a = [1, 2, 3]
list_b = list_a.copy()
print(list_b)

list_b = list_a
list_b[0] = 100
print(list_b)
print(list_a)
```
[1, 2, 3]
[100, 2, 3]
[100, 2, 3]
`list_a`が`list_b`の値に自動的に上書きされてしまっています。

:::message alert
`list_b = list_a`とすると、`list_b`が見ているデータの先と、`list_a`が見ているデータの先が同じ物になってしまう。
`copy()`を使用してからそれぞれの値を変更すれば、別々の値にすることが可能になる。
:::

```python: copy
list_a = [1, 2, 3]
list_b = list_a.copy()
print(list_a)
print(list_b)

list_b[0] = 100
print(list_b)
print(list_a)
```
[1, 2, 3]
[1, 2, 3]
[100, 2, 3]
[1, 2, 3]
無事、別々の値が出力されました。


## 2. キュー
#### 2-1. キューとは
- First in First out
- 先に入れたデータを先に出す

#### 2-2. キューの使い方
`from collections import deque`
> `collections`モジュールから`deque`というクラスをインポートすると使えるようになります。

```python: que
from collections import deque

queue = deque(["hello", "world"])
queue.append("Python")
print(queue)

print(queue.popleft())
print(queue)
```
deque(['hello', 'world', 'Python'])
hello
deque(['world', 'Python'])

1. `queue = deque(["hello", "world"])`で`queue`にデータを2つ入れます。
2. `append()`でデータを1つ追加します。
3. `popleft()`とすると、データが取り出せます。一番最初に入れた`hello`が取り出されているのが分かります。


## 3. リスト内包表記
#### 3-1. リスト内包表記とは
- Python独特の書き方
- for文の特殊パターン
  - 短い文字数で記述できる
  - パフォーマンスの向上が見込める
  - ※python初学者には読みにくい

#### 3-2. for文で書いた場合
- `data`に0~9を1つずつ追加する
1. 通常の書き方で書いた場合

```python: for(normal)
data = [] # 空のリストを宣言
for i in range(10):
  data.append(i)
print(data)
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

2. リスト内包表記で書いた場合
0~9を持つリストを生成する

```python: for(list comprehension)
data = [i for i in range(10)]
print(data)
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
シンプルで短いコードで表現出来る。

#### 3-3. for文からリスト内包表記への書き換え方
```python:
data = []  # 空のリストを宣言
for i in range(10):
    data.append(i)

# step1(空のリストを宣言)
data = []

# step2(for i in ~をリスト内に持ってくる)
data = [for i in range(10)]

# step3(追加する値iを先頭に書く)
data = [i for i in range(10)]
```

#### 3-4. リスト内包表記の読み解き方
- 書き換え方と手順は変わらない。
`data = [i for i in range(10)]` を読み解く。

1. リストであることに注目する
`data = []`

2. ループに注目
`for i in range(10)`

3. 取り出すデータに注目
`i`
※この`i`の部分は「式」と考えた方が良さそうです。


## 4. del
#### 4-1. delとは
- データを削除する
- popとの違いは、データを返さない

```python: del
list_num = [1, 2, 3]

del list_num[0] # index0を削除 -> 1を削除
print(list_num)
```
[2, 3]

#### 4-2. リスト内を全部削除する(== clear)
- clearと同じ挙動
- スライシングを使う

```python: del
list_num = [1, 2, 3]
del list_num[:]
print(list_num)
```
[]

:::message alert
`del list_num`とすると、`list_num`自体が削除されてしまうので、`NameError: name 'list_num' is not defined`のエラーが出力されます。

`del`と使うとデータへアクセスする事が出来なくなるが、直前で宣言したデータを解放するわけではない。
pythonのメモリ管理は自動で行われるため、delを用いてメモリを節約するといった事は必要ない。
`pop`や`clear`というリストに付随するメソッドで対応が可能。
:::


## 5. タプル
#### 5-1. タプルとは
- 変更不能なリスト
- タプルの特徴
  - 宣言時のデータを作る
  - 以降は参照のみ可能
  - インデックスを指定してアクセス可能
  - 要素を変更できない

#### 5-2. タプルの宣言と要素へのアクセス
- タプルの宣言は小かっこ()で行う
- インデックスを指定して出力する

```python: tuple
data = (1, 2, 3)
print(data[0])
```
1

#### 5-3. タプルは変更することが不可能
```python: tuple
data = (1, 2, 3)
data[0] = 10
```
> TypeError: 'tuple' object does not support item assignment
**ここがタプルとリストの大きな違いです。**

#### 5-4. タプルの使い所
:::message
リストより機能が少ないのであれば使い所がないと感じるかもしれないが、以下のメリットがある。

変更する必要がないデータをタプルにすることによって、別の処理で意図しない変更を防ぐ事が出来る。
特に複数人での開発の際に、別の処理で意図しない変更を防ぐ事が出来るので、バグの発生を減らす事ができ、これは大きなメリットです。
:::


## 6. 集合 set
#### 6-1. 集合とは
- リストの特殊なパターン
- 特徴
  - 重複しない
  - 順不同
  - {}を使用する

#### 6-2. 集合を使うメリット
- 集合同士の計算が出来る
  - 和: 集合Aもしくは集合B
  - 差: 集合Aに存在し、集合Bにはない
  - 交差: 集合Aにも集合Bにもある
  - 対象差: 集合Aまたは集合Bに共通しない

#### 6-3. 和: 集合Aもしくは集合B
aとbのどちらにもある要素を集約(重複は取り除かれる)

```python: set
a = {1, 2, 3}
b = {1, 4}

print(a | b)
```
{1, 2, 3, 4}

#### 6-4. 差: 集合Aに存在し、集合Bにはない
1. aに存在し、bにはない場合
2. bに存在し、aにはない場合

```python: set
a = {1, 2, 3}
b = {1, 4}

print(a - b)
print(b - a)
```
{2, 3}
{4}
