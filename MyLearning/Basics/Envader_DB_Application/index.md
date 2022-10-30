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

理解しやすい。
既存のテーブルから欲しいカラムだけ抽出して新しいテーブルを作る感じ。

- ビューの作成
`create view <ビューの名前> as select <カラム名> from <テーブル名>`

- 作成したビューの確認
`select * from <作成したビューの名前>`

- 問題2
基準となるカラム、平均にしたいカラムと分けて考える。
いまいちメソッドが理解できていない。

## 8. トランザクション

- トランザクションの確定

1. `begin;`: トランザクション開始
2. sql命令
3. sql命令
4. `commit;`: トランザクション確定

- トランザクションの取り消し

1. `begin;`: トランザクション開始
2. sql命令
3. sql命令
4. `rollback;`: トランザクション取消

## 9. レプリケーション

元から存在していたデータを別のMySQLに複製すること。

1. プライマリ上でレプリケーション化のための設定を行う
`ssh ~`

```cnf: /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
server-id=1 # 各MySQLインスタンスに割り振る固有のID
log-bin=mysql-bin # MySQLでの変更履歴を記録しておくログを保管するファイル名
```

2. 設定の反映
`sudo service mysql restart`

3. プライマリ上でレプリケーションに接続する専用のユーザを作成する
プライマリのDBに接続後。

```sql:
# replという名前のユーザを作成
CREATE USER 'repl'@'%' IDENTIFIED BY 'repl_pass';

# replにレプリケーション用の権限を付与
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

# 変更を反映
FLUSH PRIVILEGES;
```

4. プライマリからフルバックアップを取得する。
セカンダリに戻る？
`mysqldump -u <ユーザ名> -h <プライマリのipアドレス> -p --all-databases --master-data > dump.sql`

5. セカンダリ上でレプリケーション化のための設定を行う

```sql: /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
server-id=2
```

6. セカンダリの設定を反映
`sudo service mysql restart`

7. セカンダリのDBに接続する

```sql:
# dump.sqlという名前のバックアップを反映させる。
source dump.sql

# 変更結果を反映する
FLUSH PRIVILEGES;
```

8. 指定する際に必要な情報を取得する

`grep "^CHANGE MASTER" dump.sql`
MASTER_LOG_FILEとMASTER_LOG_POSの値が出力
