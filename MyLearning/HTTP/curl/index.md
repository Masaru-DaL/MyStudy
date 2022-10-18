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

ftp://と続けてファイルパスを指定すると、ファイルの内容が標準出力に表示される。
