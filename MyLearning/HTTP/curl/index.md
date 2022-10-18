# HTTP通信について細かく調べる＋curlコマンドを使って色々してみる
* curlコマンド
様々な通信プロトコルでデータの送受信を行うことができるコマンド。
CLIで `curl <url>` と叩くとWebサイトのコンテンツがテキストで表示される。

参考: [curl tutorial](https://github.com/curl/curl/blob/master/docs/MANUAL.md)

今回はcurlコマンドを一通り試してみる。

## 1. Simple Usage

1. サーバから該当Webサイトのページを取得する。
 `curl https://www.example.com/`

2. FTPサーバからREADMEファイルを取得する。
 `curl ftp://ftp.funet.fi/README`

ftpはファイル転送用のプロトコル
ftp://と続けてファイルパスを指定すると、ファイルの内容が標準出力に表示される。

3. ポート8000を使ってサーバからWebページを取得する。
 `curl http://www.weirdserver.com:8000/`

自身のポートではなく、指定しているのはサーバのポート番号

4. FTPサーバを対象にディレクトリ一覧を取得する。
 `curl ftp://ftp.funet.fi`

FTPサイト自体を指定すると、ディレクトリ一覧を取得できる。
FTPサイトのディレクトリを指定すると、そのディレクトリ内の情報が取得できる。

5. 辞書でcurlの定義を調べる。
 `curl dict://dict.org/m:curl`

dictは辞書検索用のプロトコル
`m` は'match'と'find'のエイリアス
