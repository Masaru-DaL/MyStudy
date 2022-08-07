# ToDoアプリケーションの作成 -Flask-
Flask + MySQL を使用してToDoアプリケーションを作成します。
参考: [TODO LIST FLASK APP IN 30 MINUTES](https://tichung.com/blog/2021/20200323_flask/)

:::message
環境構築はDockerで行なってあるものとします。
[Flask + MySQL (Docker) の環境構築](https://zenn.dev/articles/556d3f3864cf51/edit)
:::

## 1. Flaskアプリケーションの実行
```c: ファイル構造
demo
├── app/
│   └── __init__.py
└── main.py
```

#### 1-1. main.py
```python: main.py
from app import app

if __name__ == '__main__':
  app.run(debug = True)
```

1. appモジュールのimport
2. このpython自身が直接呼ばれているかを条件としている
3. 呼ばれた場合にapp.runを実行
   1. app.run()関数の引数に、`debug=True`を渡すことで、デバッグ出力機能を有効とする


#### 1-2. __init__.py
```python: app/__init__.py
from flask import Flask

app = Flask(__name__)
```

1. flaskモジュールのimport
2. このモジュール内にアプリケーションをカプセル化する
   1. このappは`main.py`です。
   2. 独立したモジュールであるため、Flaskを使用してこのモジュールを実行する

#### 1-3. ターミナルで定義し、起動
```c: terminal
export FLASK_APP=app
export FLASK_DEBUG=1
flask run --host 0.0.0.0 --port 5000
```

1. flask appモジュールがappフォルダにあることをターミナルに伝えている
2. 変更時にサーバを再読み込みするようFlaskに指示する
3. ローカルホスト、ポート5000でFlaskを起動する
   1. (docker-compose.ymlで何番ポートを使用するかに依存する)


#### 1-4. サーバに応答してもらう
前段階まででFlaskは実行するモジュールを認識したが、サーバが何をすべきか分からない状態になっています。
`route("/")`にアクセスするとサーバにOKという応答をしてもらうよう`__init__.py`を変更します。

:::message
Flaskのパッケージの一部である、jsonifyというモジュールをimportします。
JSON形式で表示されます。
:::

```python: __init__.py
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
  return jsonify({"status": "OK"})
```

ファイルを保存すると、サーバが再起動されるので、`{"status": "OK"}`を変更してブラウザを再読み込みすると変更が反映されます。


## 2. Flaskでhtmlファイルを提供する
```c: ファイル構造
demo
├── app/
│   ├── templates/
│   │   └── index.html
│   └── __init__.py
└── main.py
```

:::message alert
templatesディレクトリ名は変更すると上手く読み込まれなくなります
:::

#### 2-1. htmlをrenderする
```html: index.html
<h1>Hello Bob!</h1>
```

```python: __init__.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template("index.html")
```

- render_template
引数にhtmlファイルを指定すると、htmlをレンダリングして返してくれる。

再読み込みするとhtmlファイルに記述した内容が表示される。

## 3. flaskで動的htmlファイルを提供する
最終段階は、動的情報をサポートするhtmlを提供すること

#### 3-1. 動的なhtmlファイル
```html: index.html
<h1>Hello {{name}}!</h1>
```

```python: __init__.py
@app.route("/")
def homepage():
  return render_template("index.html", name="Alice")
```

:::message
index.htmlをjinjaテンプレート形式に変更します。
jinjaは**python用の、htmlを動的作成できるテンプレートエンジン**のことです。
:::

{{name}}は、レンダリングエンジンが置き換える変数を意味する。
`name="Alice"`を変更すると{{name}}も変更される。


## 4. データベースを利用する
次のロジックを実現したいと考える。
1. クライアントがサーバにリクエストを送信
2. サーバがデータベースにクエリを送信
3. データベースがデータを返す
4. サーバがデータを含むhtmlをレンダリング
5. クライアントのフロントエンドに最終的なhtmlを提供

#### 4-1. ファイル構造を更新
```c: ファイル構造
demo
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── routes.py
│   ├── database.py
│   └── __init__.py
└── main.py
```


