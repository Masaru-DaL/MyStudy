# CURLコマンドを理解する
`https://raretech.site/users` -> URL
細かくすると、
`https` -> スキーム
`raretech.site` -> ドメイン / ホスト名
`users` -> パス

-> プロトコル = ルール

`https://raretech.site(:80)/users`
ポート番号が隠れている

## クライアントサーバーモデル
クライアント - リクエスト -> サーバー
クライアント <- レスポンス - サーバー

- httpプロトコルのリクエストメッセージ
  - GET(=READ)
  - POST(=CREATE)
  - DELETE
  - PUT(=UPDATE)

- レスポンスメッセージ
  - 100, 200, 300, 400, 500番台

**CRUD**
GET, POSTなどはメソッドと呼ぶ。
リクエストの中身(書き方)は決まっている。

user-agent -> アクセス元(google, yahoo, curlの場合も)

レスポンスを受け取る自PCのポートは1万番以上などの番号

- GET
  - URLに値が見える
  - 他の人に送れる
  - ブックマークできる

- POST
  - URLに値が見えない
  - 他の人に知られたくない
  - パスワードなど
