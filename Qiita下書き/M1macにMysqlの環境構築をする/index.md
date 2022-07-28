# Docker環境構築
参考: [【M1 Pro/Max対応】M1 Mac環境構築ベストプラクティス](https://qiita.com/c60evaporator/items/aef6cc1581d2c4676504#docker%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)

こちらのDocker環境構築を参考にさせて頂きます。
無事bashが立ち上がればOKです。
あくまでもテスト的に行っただけなので、実際のDocker環境構築は次に書いていくものを行っていきます
作成したディレクトリごと削除してしまっても構いません。

## DockerでPythonの環境構築
参考: [【Python入門・応用】MacにPythonができる環境をつくろう｜02.Pythonの環境構築](https://kino-code.com/python_environment_for_mac-2/)
YOUTUBE版: [【2022最新版】M1MacにPythonの環境構築｜通常のインストール方法、Dockerを使う方法も解説](https://www.youtube.com/watch?v=6b6uM7Fl8ck&t=10s)

自分はDockerで環境構築を行いましたが、ローカルで行うかは好みで良いと思います。
Jupter Labはあまり使わなさそうで、VScodeのRemote-Containerがメインになりそうです。
自分はYOUTUBE通りに行い、特にエラーはなく構築出来ました。

## Djangoの環境構築(Docker)
遅かれ早かれ使うと思うので構築していきます。
本命は次に構築するMYSQLです。

参考: [【Python+Django4】VS Code+Dockerで簡単構築【リモート開発】【Win/Mac】 | チグサウェブ](https://chigusa-web.com/blog/django-vscode-docker/)

特にエラーも出ずに済みました。
次にDockerにMYSQLの環境を作っていきたいと思います。

参考: [【Django】DockerコンテナにMySQL/phpMyAdminを追加 | チグサウェブ](https://chigusa-web.com/blog/django-docker-mysql/)

このまま進めるとエラーが起こります
M1特有のエラーみたいなので、こちら[M1 MacによるDocker開発環境構築エラー](https://qiita.com/prkrsign890/items/10ecb57e0387a673b3a2)を参考に、
docker-compose.ymlに、`platform: 'linux/amd64'`を記述してコンテナのビルドを行ってください。


# まとめ
今回はDocker + Python, Docker + Django + MYSQL の環境構築を行いました。
他の方の記事が素晴らしすぎて、記事の通りに進めていくだけで環境を構築することができました。
特にエラーもなく、M1macにDockerが対応してきていてありがたいな〜という気持ちです。
