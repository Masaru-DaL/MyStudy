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
