# Docker + Flask + MySQLの環境構築
基本的な流れは以下の記事を参考に進めていきます。
参考: [flask + mysql の環境をDocker（docker-compose）で構築する](https://www.anypalette.com/ja/posts/20191201_flask-docker/)

:::message alert
- M1mac特有の2つのエラーを解消するのがキモ
1. docker-compose.ymlファイル
2. デフォルト使われているポート5000への対応
:::

## 1. docker-compose.ymlファイル
参考記事のdocker-compose.ymlファイルに`platform: linux/amd64`を追記する。
M1macのプラットフォームはarm64なので明示的に明示的にamd64のイメージを取得するようにします。
追記したのが以下のコード

```c: docker-compose.yml
version: "3"
services:
  web:
    platform: linux/amd64
    build: ./flask
    volumes:
      - ./flask:/app
    ports:
      - 5000:5000
    links:
      - db
    tty: true

  db:
    platform: linux/amd64
    build: ./db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: flask
      MYSQL_USER: flask
      MYSQL_PASSWORD: flask
      TZ: 'Asia/Tokyo'
    command: mysqld --character-set-server=utf8mb4 --collation-server=utf8mb4_bin
    volumes:
      - ./db/data:/var/lib/mysql
      - ./db/my.cnf:/etc/mysql/conf.d/my.cnf
      - ./db/sql:/docker-entrypoint-initdb.d
      - ./db/log:/var/log/mysql
    ports:
      - 3306:3306
```

## 2. デフォルト使われているポート5000への対応
buildしてupした際に5000ポートが既に使われていますというエラーメッセージが出力されます。
ネットワークユーティリティ(GUI)は現在使用出来ず、ターミナルで5000ポートを確認します。

`lsof -i:5000`
何かしらが動いているのが確認できます(エラーメッセージからデーモンが動いているのが分かります。)

killして再度確認してもデーモンなので再度動いているのが分かります。
調べた感じこちらの記事がヒットしました。
[MacをMontereyにアップデートしたらFlaskが5000番ポートで起動できなくなった](https://www.keisuke69.net/entry/2021/10/29/012608)

Flaskの指定ポート5000を変更するか、対応アプリケーションのチェックを外すかのどちらかみたいです。
今のところアプリケーションの使用予定がないので自分はチェックを外して再度upすると無事コンテナが起動しました。
