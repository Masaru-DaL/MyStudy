# パスワードリセット機能の確認まで
## tinkerでテストメールの送信

![picture 1](../../images/c4a55358ce3a8fea4d6752eb044804ff9e514b26cf938f0ff501e64588c36b9b.png)

.envに記述してtinkerでコマンドを打ってnullが返って来たら成功

(パスワードはGoogleの２段階認証 -> アプリケーションのパスワードを設定し、そのパスワードをMAIL_PASSWORDに設定する)
※gitignoreに.envが適用されてるか確認！


## mailhogを使ったテスト!
### mailhogの導入
docker-compose.ymlに追加
![picture 2](../images/6258f2836c505f54dfd88f4d9e61bada7f2ab2fcdd82952a91644a9208fe8596.png)


[picture 1](../images/9c5b80d64aaec4b9361851ce6baf9c9a40683a90052fc40a6bba81c618725052.png)

### src/.envに記述
![picture 3](../images/d617132488bb32cc8e035c66822b6249bef58932c573ac33cd700ef729c6fff1.png)

MAIL_FROM_ADDRESS は何でも良い。

` docker-compose exec php php artisan tinker`
`Mail::raw('test mail',function($message){$message->to('test@example.com')->subject('test');});`

`=> null`
が返ってくればOK

mailhogで確認するとメールが返ってくる。
