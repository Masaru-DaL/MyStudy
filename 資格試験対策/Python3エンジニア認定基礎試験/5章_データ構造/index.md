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

####
