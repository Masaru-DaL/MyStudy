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
