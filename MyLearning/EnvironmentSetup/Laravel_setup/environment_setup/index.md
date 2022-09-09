# RareTech ハッカソン Team:RAT-X=5
# 環境構築
## 構築手順
YasuY1 — 2022/04/29
【Laravelの始め方　その①】
〜Composerをインストールしよう！〜
Laravelをインストールするには、ComposerというPHPのパッケージ管理アプリのインストールが必要です。
先ずは公式からダウンロードしましょう。
http://getcomposer.org/

インストールが完了したら、composerをダウンロードディレクトリから/usr/local/bin配下に移動させます。
sudo mv composer.phar /usr/local/bin/composer

次に、実行権限を追加します。
実行できる状態の場合は飛ばしてください。
いちおう青本では全てのユーザーに対して実行権限が付加されています。
chmod a+x usr/loca/bin/composer

ここまでできたらいよいよLaravelのインストールです。
composer global require "laravel/installer=~1.1"

環境変数を追加しましょう。
echo "export PATH=~/.composer/vendor/bin:PATH" >> ~/.bash_profilesource ~/.bash_profile
zshの場合はおそらくzshrcかな？

作業ディレクトリに移動した上で
composer create-project laravel/laravel アプリ名 --prefer-dist

作ったアプリの中へ移動した上で
php artisan serve

これでlocalhost:8000にLaravelの画面が表示されればOK！
MAMPの場合は8080
Composer
A Dependency Manager for PHP

***

@YasuY1が貼ってくれたこの手順で進めたが、
$ php artisan serve
でエラーが発生。

調べた所、[こちら](https://ja.stackoverflow.com/questions/28239/laravel5-1-%E3%81%A7-php-artisan-serve-%E6%99%82%E3%81%AB%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E5%87%BA%E3%81%A6%E3%81%97%E3%81%BE%E3%81%84%E3%81%BE%E3%81%99)で同じエラー内容を発見。

$ compose update
は試していたので、
$ compose install
を試した所、上手く行かなかったので、
$ sudo apt install php-xml
を行い、その次に再度
$ compose install
を試すと上手くインストールが進み、

$ php artisan serve
でlocalhost:8000が接続可能になる。


