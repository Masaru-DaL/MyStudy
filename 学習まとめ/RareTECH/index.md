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

**CRUD**
GET, POSTなどはメソッドと呼ぶ。
リクエストの中身は決まっている。
