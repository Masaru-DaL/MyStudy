- [クリーンアーキテクチャ](#クリーンアーキテクチャ)
  - [1. クリーンアーキテクチャという概念が生まれた背景](#1-クリーンアーキテクチャという概念が生まれた背景)
  - [2. クリーンアーキテクチャを採用するメリット](#2-クリーンアーキテクチャを採用するメリット)
    - [2-1. 副次的なメリット](#2-1-副次的なメリット)
  - [3. 図を理解する](#3-図を理解する)
    - [3-1. Entities(Enterprise Business Rules)](#3-1-entitiesenterprise-business-rules)
    - [3-2. Use Cases(Application Business Rules)](#3-2-use-casesapplication-business-rules)
    - [3-3. Controllers, Gateways, Presenters(Interface Adapters)](#3-3-controllers-gateways-presentersinterface-adapters)
    - [3-4. Devices, Web, UI, DB, External Interfaces(Frameworks & Drivers)](#3-4-devices-web-ui-db-external-interfacesframeworks--drivers)
    - [3-5. 円の左側から内側に向かっている矢印](#3-5-円の左側から内側に向かっている矢印)
    - [3-6. 依存関係を守らない場合](#3-6-依存関係を守らない場合)
# クリーンアーキテクチャ

参照: [実装クリーンアーキテクチャ](https://qiita.com/nrslib/items/a5f902c4defc83bd46b8)
参照: [クリーンアーキテクチャが何のためにあるのか分からない人へ](https://qiita.com/juchilian/items/d732afab315e3c7e8ba3)

## 1. クリーンアーキテクチャという概念が生まれた背景

- 例から学ぶ
プロジェクトディレクトリを開いた時に必要な情報は、「どのフレームワークを使っているか」や「どういうファイル構成か」ではない。**このシステムは何をしてくれるのか**?が分かる事が重要。

> フレームワークはあくまでツールであることを強調しています。
> さらに深掘りするとWebもあくまでツールであると主張しています。
> Webは重要な要素でなく単なるインプットを受け取ってアウトプットを返すためのインターフェースに過ぎないということです。

> なぜなら、解決するべき課題、クリーンアーキテクチャ風に言うと「ビジネスロジック」はインターフェースが何であろうが不変だからです。

[参考: ビジネスロジック image](https://camo.qiitausercontent.com/74cd33ee0437c49f8169ee1ad341675e407b7274/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3435303235372f65376239303861392d333164622d383337332d313539382d3737623061396165343836612e706e67)

注文を受ける時に必要な情報は、それを受け取る場所がWebブラウザであろうが、コンソールであろうが、電話であろうが変わらない。受け取った情報を使って注文を作成する手順も同じ。

これが、**根底にあるビジネスロジックは、不変である**ということ。

## 2. クリーンアーキテクチャを採用するメリット

- ビジネスロジックを中心に添えて開発をすることで、FWやUIに依存しないアプリケーションを作ることができる。
  - WebやDBにすら依存しないアプリケーションが作れる。
依存しないという事は、将来FWやUIの変更をしても根底にあるビジネスロジックを書いたコードは変わらず生き残り続ける。

- 結論
**クリーンアーキテクチャを採用することで、将来の変更に強いアプリケーションを作ることが出来る。**

### 2-1. 副次的なメリット

- ビジネスロジックが明確になる
ビジネスロジックがどこに書いてあるのかを明確にディレクトリに分けて管理するため、ビジネスロジックとその他というのが分かりやすくなる。

- テストがやりやすくなる
クリーンアーキテクチャを採用することで、以下のように**階層的にテストを行える**。

1. まずは、細かいビジネスロジック(Entities)だけをテストする
2. 次にビジネスロジックを複数まとめた一連の業務ロジック(Use Cases)をテストする
3. 最後にWebからインプットを受け取って、DBに保存など(Controllers, Presenters, Gateways)についてテストする

テストがより細かい粒度で行えるため、修正がしやすく、将来の変更にも対応しやすくなる。

## 3. 図を理解する

クリーンアーキテクチャを理解するには、よく出てくる以下の図を理解しなくてはならない。

[The Clean Architecture](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F450257%2F1a4c15a6-4f59-5c8b-6f38-47de63204e07.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=a65118a50518e199cd13cfdb3d17da1f)

### 3-1. Entities(Enterprise Business Rules)

一番中心の黄色部分(Entities)には**ビジネスロジック**が入る。
[1. クリーンアーキテクチャという概念が生まれた背景](#1-クリーンアーキテクチャという概念が生まれた背景)での画像の図で言う所の**Data**にある`Customer-id`や`Customer-contact-info`などは、この階層で定義される必要がある。

細かいビジネスロジックもEntitiesに含まれる。同じく、図で言う所の**Primary Course**にあるそれぞれ番号が書かれている処理のこと。これを番号ごとに関数で実施するイメージ。

### 3-2. Use Cases(Application Business Rules)

赤色の円部分(Use Cases)では、**細かいビジネスロジックをまとめて一連の流れとして実行する**。
具体的には**Primary Course**にあるそれぞれ番号が書かれている処理を、**1~4で順番に並べて実行するような関数を作る**。

例えば、人事システムを作るとしたら、「従業員を雇う」や「従業員を解雇する」とかの単位がUse Casesで実行される。

### 3-3. Controllers, Gateways, Presenters(Interface Adapters)

緑色の円部分(Controllers, Gateways, Presenters)では、**WebやDBに関する処理が書かれる**。(Webシステムを使いたい場合)

具体的には、DBに接続して保存する処理、Web APIの処理などが書かれる。

### 3-4. Devices, Web, UI, DB, External Interfaces(Frameworks & Drivers)

一番外の青色部分。
Devices, Web, UI, DB, External Interfacesが**ビジネスロジックから切り離されている点**が重要。

### 3-5. 円の左側から内側に向かっている矢印

この矢印は**依存関係**を示している。

- 緑 -> 赤は参照できるが、赤 -> 緑はだめ。
- 赤と黄の依存関係も同じ。

**この依存関係を守ることで、クリーンアーキテクチャが完成する**。

### 3-6. 依存関係を守らない場合

どうしても内側から外側に参照しなければならない箇所が生じた場合、[右下の図](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F293368%2F3f64e75c-c34d-6230-4646-7ea7d2acbaf2.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=0b34503c398e5d118728b430258b1448)のことを行う。この図はは以下の流れで行なっている処理を指す。

1. `UserController`が`IUserCreateUseCase`に入力データを伝える。
2. `IUserCreateUseCase`の実態である`UserCreateInteractor`に処理が移譲される
3. `UserCreateInteractor`は処理を行い、その結果を`IUserCreatePresenter`に出力データを伝える
4. `IUserCreatePresenter`の実態である`UserCreatePresenter`に処理が移譲される
5. `UserCreatePresenter`は表示を行う

ここはいまいち理解できてない...
