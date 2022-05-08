# Laravel Setup Progres
## 言語や日時の設定
言語や時刻の設定は config/app.php で設定します。

#'timezone' => 'UTC', #55行目あたり
'timezone' => 'Asia/Tokyo',

#'locale' => 'en', #68行目あたり
'locale' => 'ja',

## php:warning error
php7.4を再インストール
参考下記サイト
https://www.petitmonte.com/linux/unable-to-load-dynamic-library.html

# login画面の実装
https://qiita.com/daisu_yamazaki/items/b946594896179abcd203

npmを入れてなかったので、
https://www.deep-rain.com/programming/program/611#ubuntu1604Debian
## 発生したエラー
nmp installおよび、npm run dev

- インストールされたjsモジュールを全部消す
  - rm -rf node_modules

再度nmp installおよび、npm run dev
