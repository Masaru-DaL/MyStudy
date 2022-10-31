# GitHubとCircleCIの連携手順

## 1. 前提

- GitHubのアカウント登録
- CircleCIのアカウント登録(GitHubアカウントでサインイン)

## 2. CircleCIでHello World

参考: ****[GitHub+CircleCI入門](https://qiita.com/tatane616/items/8624e61473a9957d9a81)****

- `Hello-World`という名前で新規リポジトリを作成

### 2-1. プロジェクト作成 ~ リポジトリにプッシュまで

1. `.circleci/config.yml`を作成

```shell:
-> tree -a
.
└── .circleci
    └── config.yml

1 directory, 1 file
```

2. `config.yml`の中身

```yml:
version: 2.1
jobs:
  build:
    docker:
      - image: circleci/node:4.8.2
    steps:
      - checkout
      - run: echo "hello world!!"
```

3. `Hello-World`リポジトリにpush

### 2-2. CircleCI

1. GitHubアカウントでサインイン

2. Dashboard > Add Project

3. Hello-Worldの右の`SetUpProject`ボタンをクリック

4. Faster > Hello-World でmainを指定して`SetUpProject`ボタンをクリック

5. 自動でビルドされるようで、少し経つと"Success"となる。

6. Pipeline(Hello-World) > build(1) をクリック

## 3. CI/CDプロセス

参考: [GitHub CI/CD チュートリアル: 継続的インテグレーションのセットアップ](https://circleci.com/ja/blog/setting-up-continuous-integration-with-github/)

- 流れ

1. Flaskを使用したPythonアプリケーションの作成
2. アプリケーションのテスト
3. config.ymlファイルの作成
4. GitHubにプッシュ
5. CircleCIを構成する
6. バッジでREADMEを更新する
7. プルリクエストを作成してCircleCIの動作を確認する

### 3-1. GitHubにプッシュまで

1. `CI-CD-Process`という名前で新規リポジトリの作成

2. Flaskでファイルの作成
venvで仮想環境を作成。

```shell:
-> tree
.
├── __pycache__
└── venv
├── hello.py
└── requirements.txt
```

```python: hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

```txt: requirements.txt
Flask
```

3. `localhost:5000`でHello World!が表示。

4. テストの作成

```python: tests.py
from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World!'
    assert response.status_code == 200

print("test success") # 標準出力にも分かるように出す。
```

5. CircleCI設定ファイルを追加する。

```yml: .circleci/config.yml
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.6
    steps:
      - checkout
      - restore_cache:
          key: deps1-{{ .Branch }}-{{ checksum "requirements.txt" }}
      - run:
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      - save_cache:
          key: deps1-{{ .Branch }}-{{ checksum "requirements.txt" }}
          paths:
            - "venv"
      - run:
          name: テストの実行
          command: |
            . venv/bin/activate
            python3 tests.py
      - store_artifacts:
          path: test-reports/
          destination: python_app
```

