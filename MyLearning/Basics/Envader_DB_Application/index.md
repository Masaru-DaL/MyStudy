# Envader DB 応用コース

## 1. 集計関数

1. COUNT
2. SUM
3. MAX
4. MIN
5. AVG

- 使い方
`select count(<対象columns>) from <table名> where <条件>`

## 2. 集約

- GROUP BY

対象columnの数をカウントしたい場合(全て)
`select <対象column>, count(*) from <table名> group by <対象column>`

2つ目は理解できてない。
結合をしっかり学んだほうが良さそう。

## 3. CASE

selectと絡めるといまいち分からない。
`SELECT CASE prefecture_id WHEN 12 THEN '首都3県'`
とするとwhenの後にカラム=としなくても良い？
selectと絡めなければテーブルとカラムを指定する感じなので分かりやすい。

## 4. userの作成と権限

説明文見ながら理解できた。

- ユーザの作成
`create user '<作成するユーザ名>'@'<ホスト名:接続先(%が使える)>' identified by '設定するパスワード';`

- ユーザの一覧表示
`select user from mysql.user;`

- 権限の設定
`grant <権限名> on <対象データベース>.<対象のテーブル> to 'ユーザ名'@'ホスト名';`

## 5. DBの情報

- バージョンの確認
mysqlを起動してから。
`SELECT VERSION();`

- MySQLの状態を表示
`status`

- MySQLの文字コード変更
`/etc/mysql/mysql.conf.d/mysqld.cnf`に[mysqld]を入れてから文字コードの設定を書く必要がある。

## 6. バックアップの取得

`mysqldump`はMySQLの外で打つ。
mysqlコマンドのオプションが大事。

## 7. ビュー


