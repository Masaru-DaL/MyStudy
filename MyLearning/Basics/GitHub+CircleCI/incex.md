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


