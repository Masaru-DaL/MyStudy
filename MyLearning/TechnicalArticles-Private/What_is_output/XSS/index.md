# XSS

## 1. XSSを実際に行ってみる

### 1-1. 環境構築, Webサイトの表示

参考: [xss 脆弱性のあるサイトを作ってセッションハイジャックを試す - Qiita](https://qiita.com/ahya_emon/items/6c5afce4fb489b3404c8)

1. `brew install node`
2. バージョンチェック
`node -v` , `nmp -v`

3. `npm install express`
4. 参考サイトからDLし、フォルダへ移動
5. `node app.js`
Example app listening on port 3333

6. 参考サイト通りに一通り試してみて、概要を掴む
