# Laravelでの開発の流れ
ハッカソンでバックエンド担当としてLaravelを使用しましたので、基本的な開発の流れを書いておこうと思います。

## 前提
- 環境構築が終わっていること
  - Laravel 8.x
  - PHP 7.x

とします。

## MVCを何となく理解する
![0ea88fa012e77de8e76f47a6b3c61d9c4b7a012a73cae73c9d55639b695f12c6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2564369/b7f57dde-b07f-0107-6e1a-917306a9a7a7.png)

参考: [Laravel学習帳](https://laraweb.net/surrounding/922/)

- MVCとは
  - Model
  - View
  - Controller

の３つの事を指します。
このMVCと、ルーティング、DBがあるんだな～ぐらいで最初は大丈夫です！

## HelloWorldを表示するまでの流れ
参考: [Laravel で HelloWorld](https://qiita.com/ekzemplaro/items/c74e7431a8a90e2feb03)
バージョンが合っていませんが、こちらの流れに沿っていけば表示されますので大丈夫です。
同バージョンの場合[Laravel インストール HelloWorld](https://syslog.life/2020/10/20/laravel-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB-helloworld/)


大まかな流れとしては、
1. Controllerの作成
2. Routingの作成
3. BladeでViewの作成
4. サーバーの起動

4ステップでもう見れるんですね！
記述内容は上記の参考サイトを参考にしていただいて、ポイントを記述したいと思います。

## Controllerの作成
作成には2パターンあります。
ターミナルでコマンドを打つと作成されるパターン or 対象ディレクトリ内に手動でファイル名を打って作成するか。


- コマンドで作成
  - php artisan make:controller コントローラ名
- 手動で作成
  - app -> Http -> Controllers内に「 ~ Controller.php」という名前で作成

:::note warn
Controllerファイルはキャメルケースで最後がController.phpという名前で決める決まりがあります。
:::

## Routingの作成
Routesディレクリ内のWeb.phpに記述します。

:::note warn
※Laravel8では
```c
Route::get('hello', 'App\Http\Controllers\HelloController@index');
```
このようにAppから順にコントローラーの場所を指定しなくてはいけません。
:::

参考: [Laravel8 新しいルーティングの書き方](https://kawax.biz/laravel8-routing/)
他のアプローチや詳しい事が書いてあります。

```c
Route::get('hello', 'App\Http\Controllers\HelloController@index')->name(hello);
```
->name(名前)のように別名を付ける事が出来ますが、注意なのはControllerでは指定できません。Viewファイル(Blade)でルーティングを指定するときに指定することができます。

その際には url('/hello') -> route('hello')のように記述の仕方が変わります。
利点としてはルーティングを変更した際に名前で指定してれば、Viewファイルを書き直さなくて良いという点があります。

## Viewの作成
Resources -> viewsディレクトリ内に作成します

:::note warn
ファイル名の最後は「ファイル名.blade.php」というように名前にするのが決まりです。
bladeという名前が出てきたら「あっ、Viewファイルのことだな！」と思ってください。
:::

html, cssのような記述方法で記述可能です。
formやCSSのファイルを指定する際などに {{ }} の中に記述する場合があります。
ファサードと呼ばれる物で、筆者もまだ詳しくは分かっておりません。(奥が深いです...)
適宜必要な場合に使用していく感じで良いと思います。

## サーバーの起動
ターミナルでコマンドを打ち込む事で起動します。
環境次第でここは変わってきます。

```c
php artisan serve
```
このコマンドが基本となります。

ローカル環境の場合、
XAMPPであればXAMPPでWebサーバを立ち上げれば見れますし、
DockerであればDockerでWebサーバを立ち上げれば見れます。


# まとめ
今回はモデルに関しては触っていませんが、DBにデータを入れてそれをいじる際にモデルを作成していじっていく事になります。

MVCは最初は慣れないかもしれませんが、慣れてくるとどこに何が書いてあるのか分かりやすく、問題を切り分けて考える事が出来ますので、色々いじって慣れていきましょう！
