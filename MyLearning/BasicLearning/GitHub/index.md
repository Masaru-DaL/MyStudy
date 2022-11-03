# tigの使い方に慣れる

参考: [tigでgitをもっと便利に！ addやcommitも](https://qiita.com/suino/items/b0dae7e00bd7165f79ea)

## 1. 何はともあれ、tigと打ってみる

- `tig`
  - = `git log`
  - 表示された画面は`main view`と言う

![](2022-11-03-09-21-05.png)

-
- `main view`でenter
  - `diff view`と言う
  - `diff view`では個々のコミットの`diff`を表示することができる。
`Unstaged Changes`はまだステージに上げていない差分を見れる。

![](2022-11-03-09-24-03.png)

## 2. tigでaddする

- `main view`で`S`（`shift+s`）を押すと、`git status`の結果が表示される。（`status view`）
enterを押すとファイルの差分も見れる。

![](2022-11-03-09-38-59.png)

- ステージングしたいファイルに合わせて`u`を押すとステージングできる。
`M MyLearning/BasicLearning/GitHub/index.md`（ファイル）が`Changes not staged for commit:`から`Changes to be committed:`に移動した。
=> `git add MyLearning/BasicLearning/GitHub/index.md`

![](2022-11-03-09-40-51.png)

- tigのステージングポイント

1. グループ化されているのでグループごとにステージングできる
@@ ~ @@までがグループ化
多分グループ単位でステージング出来て、自分でどこからどこまでとかは出来なさそう（あやしい）

2. 1行単位でもステージングできる
`diff view`で`1`を押すとできるもよう。

## tigでcommitする

- `status view`で、`C`（`shift+c`）を押すと`commit`できる。
