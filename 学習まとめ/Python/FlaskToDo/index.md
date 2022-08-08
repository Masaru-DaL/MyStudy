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

#### 4-2. database.py
```python: database.py
import random

def query_name():
  return random.choice(["Alice", "Bob", "Chris", "Dolly"])
```

1. randomモジュールをimport
2. リストからランダムに抜き出す

#### 4-3. routes.py
```python: routes.py
from flask import render_template
from app import app
from app import database as db_helper

@app.route("/")
def homepage():
  return render_template("index.html", name=db_helper())
```

1. 各種モジュールのimport
   1. as でdb_helperに名前を変更している
2. htmlのrender

#### 4-4. __init__.py
```python: __init__.py
from flask import Flask

app = Flask(__name__)

from app import routes
```

1. importするモジュールのroutesが別のファイルに保存されていることをFlaskに伝えるために最後の行に記述しています。

#### 4-5. app = Flask(__name__)　の理解を深める
この`app`にはflaskアプリの核が入っているイメージ(みたいです)

- __name__
  - モジュールの属性の1つ
  - グローバル変数

この`.py`ファイルが直接起動された時は、`__name__`には`__main__`という文字列が入る。
一方で、このファイルが他のスクリプトからimportされて呼ばれた時には、`__name__`にはモジュール名(拡張子なしのファイル名)が入る。

第一引数に`__name__`を渡してFlaskクラスのインスタンスを作成し、`app`に代入している。


#### 4-6. ここからToDoアプリに変換するためには
:::message
1. `index.html`をtodoリストのhtnlに更新する
2. `route.py`に、フロントエンドのJavaScriptとバックエンドのURLを橋渡しをさせる。
3. `database.py`ファイルが実際のクエリのためのデータを返すように、データベースに接続する
:::

## 5. フロントエンドコードの確立
#### 5-1. route.py
```python: routes.py
@app.route("/")
def homepage():
	return render_template("index.html")
```

1. `routes.py`をhtmlのみを返すように変更する。

#### 5-2. ファイル構造の更新
```c: ファイル構造
demo
├── app/
│   ├── static/
│   │   ├── script/
│   │   │   └── model.js
│   │   ├── styles/
│   │   │   └── custom.css
│   │   └── index.html
│   ├── templates/
│   │   └── index.html
│   ├── routes.py
│   ├── database.py
│   └── __init__.py
└── main.py
```

#### 5-3. index.html, custom.css の更新
```html: index.html
<!DOCTYPE html>

<html>
    <head>
        <title>Demo: TODO</title>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="icon" href="{{ url_for('static', filename='img/cs.ico') }}">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.css">
        <link rel="stylesheet" href="{{ url_for('static', filename='styles/custom.css') }}">
    </head>

    <body>

    <main role="main" class="container extra-bottom">
      <h1 class="mt-5">TODO List Demo App</h1>
      <p><mark>Do it now.</mark></p>
    </main>


    <div class="container">

        <!-- Button trigger modal -->
        <div style="text-align: right;">
        <button type="button" class="btn btn-outline-info btn-sm" data-bs-toggle="modal"
														data-bs-target="#task-modal" data-source="New Task">Add Task</button>
        </div>


        <div class="modal fade" id="task-modal" tabindex="-1" aria-labelledby="Label" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="Label">Add a task</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                <div class="input-group mb-3">
                    <span class="input-group-text" id="task-form-display">Task</span>
                    <input type="text" class="form-control" placeholder="Description of task"
													aria-label="task-name" aria-describedby="basic-addon1">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button id="submit-task" type="button" class="btn btn-primary">Save changes</button>
            </div>
            </div>
        </div>
        </div>

    </div>

    <!--Todo Table-->
    <div class="container table-responsive">
    <table class="table">
        <thead>
        <tr>
            <th class="task-id">#</th>
            <th class="task">Task Name</th>
            <th class="status">Status</th>
            <th class="update">Edit</th>
            <th class="update">Remove</th>
        </tr>
        </thead>

        <tbody>
            <tr>
                <td>1</td>
                <td>task1</td>
								<td><button type="button"
														class="btn btn-outline-warning btn-sm state"
														data-source="1">Todo</button></td>
                <td>
									<button type="button" class="btn btn-outline-info btn-sm"
													data-bs-toggle="modal" data-bs-target="#task-modal"
													data-source="1" data-content="task1">
										<i class="fa fa-pen fa-1" aria-hidden="true"></i>
									</button>
								</td>
                <td><button class="btn btn-outline-secondary btn-sm remove"
														data-source="1" type="button">
									<i class="fa fa-trash fa-1" aria-hidden="true"></i>
										</button>
								</td>
            </tr>
						<tr>
                <td>2</td>
                <td>task2</td>
								<td><button type="button" class="btn btn-outline-warning btn-sm state"
														data-source="2">Todo</button></td>
                <td>
									<button type="button" class="btn btn-outline-info btn-sm"
												  data-bs-toggle="modal" data-bs-target="#task-modal"
													data-source="2" data-content="task2">
										<i class="fa fa-pen fa-1" aria-hidden="true"></i>
									</button>
								</td>
                <td><button class="btn btn-outline-secondary btn-sm remove" data-source="2" type="button">
									<i class="fa fa-trash fa-1" aria-hidden="true"></i>
										</button>
								</td>
            </tr>

        </tbody>
    </table>
    </div>

    <footer class="footer">
      <div class="container">
            <p class="text-muted"><small>App developed for CS411 UIUC by @tcheng10</small></p>
      </div>
    </footer>
  </body>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='script/modal.js') }}"></script>

</html>
```

```css: custom.css
html {
    position: relative;
    min-height: 100%;
}

body {
    /* Margin bottom by footer height */
    margin-bottom: 2em;
}

.footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 2em;
    /* Set the fixed height of the footer here */
    line-height: 1.5em;
    /* Vertically center the text there */
    background-color: #f5f5f5;
}

hr {
    width: 50%;
    margin: auto;
}

.table td {
    text-align: center;
    vertical-align: middle;
}

.table tr {
    text-align: center;
    vertical-align: middle;
}

/* bootstrap modifications */
.container {
    width: auto;
    max-width: 680px;
    padding: 0 15px;
}

.extra-bottom {
    padding-bottom: 2em;
}

.task {
    width: 50%;
}

.task-id {
    width: 10%;
}

.status {
    width: 20%;
}

.update {
    width: 10%;
}
```

1. 現在は静的な状態
2. ToDoリストとして機能するために動的にしなくてはいけない

#### 5-4. 次に行うことの整理
:::message
1. ToDoリストテーブルがサーバからの動的タスクをレンダリングするようにする
2. ボタンを押した時の動作を機能するようにする
:::

## 6. 動的なhtmlへの更新
#### 6-1. index.htmlの変更
```html: index.html
<tbody>
        {% for item in items %}
            <tr>
                <td>{{item.id}}</td>
                <td>{{item.task}}</td>

                {% if item.status == "In Progress" %}
                    <td><button type="button" class="btn btn-outline-warning btn-sm state"
														data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}
                {% if item.status == "Todo" %}
                    <td><button type="button" class="btn btn-outline-secondary btn-sm state"
														data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}
                {% if item.status == "Complete" %}
                    <td><button type="button" class="btn btn-outline-success btn-sm state"
														data-source="{{item.id}}">{{item.status}}</button></td>
                {%endif%}

                <td><button type="button" class="btn btn-outline-info btn-sm" data-bs-toggle="modal"
														data-bs-target="#task-modal" data-source="{{item.id}}"
														data-content="{{item.task}}"><i class="fa fa-pen fa-1" aria-hidden="true"></i>
										</button></td>

                <td><button class="btn btn-outline-secondary btn-sm remove" data-source="{{item.id}}"
														type="button"><i class="fa fa-trash fa-1" aria-hidden="true"></i>
										</button></td>
            </tr>
        {% endfor %}
</tbody>
```

1. 動的なToDoリストに対応するために、テーブル本体をjinjaに置き換える
2. items->itemに渡す
   1. itemにはID, タスクの説明、状態(Todo, Complate, In Progressのいずれか)を持つものとします。(DBとの連携)

#### 6-2. routes.py, database.py の更新
```python: routes.py
@app.route("/")
def homepage():
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)
```

```python: database.py
def fetch_todo():
    todo_list = [
			{"id": 1, "task": "Task 1" , "status": "In Progress"},
			{"id": 2, "task": "Task 2", "status": "Todo"},\
		]
    return todo_list
```

1. `database.py`にtodoリストを返す関数を記述
2. `routes.py`のhomepage関数
   1. items変数に①を入れる

:::message
動的に対応するために、jinjaを使用しています。
htmlで変数を利用するには、`render_template`の第2引数以降で変数を埋め込むことで使用出来ます。
`items=items`とすることで、index.htmlの変数で利用出来ます。
:::


## 7. CRUD操作をサポートするルートの追加, JavaScriptの追加
#### 7-1. ルートの追加(routes.py)
```python: routes.py
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:task_id>", method=['POST'])
def delete(task_id):
  try:
    result = {'success': True, 'response': 'Removed task'}
  except:
    result = {'success': False, 'response': 'Something went wrong'}

  return jsonify(result)


@app.route("/edit/<int:task_id>", method=['POST'])
def update(task_id):
  data = request.get_json()
    print(data)
  try:
    if "status" in data:
      result = {'success': True, 'response': 'Status Updated'}
    elif "description" in data:
      result = {'success': True, 'response': 'Task Updated'}
    else:
      result = {'success': True, 'response': 'Nothing Updated'}
  except:
    result = {'success': False, 'response': Something went wrong}

  return jsonify(result)


@app.route("/create", method=['POST'])
def create():
  data = request.get_json()
  result = {'success': True, 'response': 'Done'}
  return jsonify(result)


@app.route("/")
def homepage():
  items = db_helper.fetch_todo
	return render_template("index.html", items=items)
```

- 例外処理
try: エラーが発生するかもしれないプログラム
except: 例外発生時に行いたいプログラム
※tryとexceptはセットで使用する

- in演算子
`x in y`
xがyにあるかどうかを判定して、TrueもしくはFlaseを返す

#### 7-2. JavaScriptを定義してURLを呼び出す

- jQuery

```c: javascript
$(document).ready(function(){
  //何かしらの処理
});
```

> これは画像などを除いて、HTRL=DOMの読み込みが終わったらfunction()の中の処理(=なにかしらの処理)を実行するという意味です。

- bootstrap modal

```c: javascript
$('#task-modal').on('show.bs.modal', function (event) {
    // 何かしらの処理
  });
```

> bootstrapに用意されているイベントを使用している
> 何かしらの処理が実行されたら実行されるイベント
> [Modal](https://getbootstrap.jp/docs/4.2/components/modal/#events)
