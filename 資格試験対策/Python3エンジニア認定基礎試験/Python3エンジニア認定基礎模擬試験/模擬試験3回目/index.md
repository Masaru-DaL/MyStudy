## range(5)
`print(range(5))`
-> range(0, 5)

## remove(の挙動
- remove()
  - 引数に指定した数を対象のindex0から数えて一番最初に見つかった数を削除する

`list = [5, 3, 1, 2, 3, 4, 5, 2]`
`list.remove(2)`
`print(list)`
[5, 3, 1, 3, 4, 5, 2]

## count()
- count()
  - 引数に指定した値が何個あるか数える

`num_list  = [2, 4, 6, 4, 4, 2, 6]`
`for i in range(num_list.count(4)):`
    `print(i, end=' ')`
0 1 2
`for i in range(3)`と同じ

- range(num_list.count(4))
  - num_listに4がある数分繰り返す処理となるので、3回繰り返すという意味

## リスト内包表記
`[(x, y) for x in [0,1,2] for y in [1,2,3] if x != y]`

`if x != y`の時、`(x, y)`に追加する。
0 1, 0 2, 0 3, 1 2, 1 3, 2 1, 2 3

## 要素の削除
- del
  - インデックスやスライスで位置・範囲を指定して削除する


## タプル
- タプルの作成
t = 要素1, 要素2, ...
-> (要素1, 要素2, ...)

## 変数
