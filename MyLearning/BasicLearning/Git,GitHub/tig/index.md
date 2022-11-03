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

## 3. tigでcommitする

- `status view`で、`C`（`shift+c`）を押すと`commit`の画面が表示される。
一番上の場所にコミットメッセージを書いて`:wq`を押すとコミットが完了する。
=> `git commit -m 'First Commit of tig`

![](2022-11-03-09-58-45.png)

## 4. tigでpushする

**tigでpush, pullができないもよう**
気合いで出来なくはないが、tigはあくまでもビュワーの役割みたい。

## 5. tigは慣れるまで大変

`main view`で`h`を押すとヘルプ画面になるので、そこを見ながら覚えていく形が良さそう。

![](2022-11-03-10-06-37.png)

コミットしようとして`shift+c`と間違えて`ctrl+c`を押すと強制終了した。


test
