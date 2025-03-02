# CI/CD と DevOps

## 1. CI/CDとは

- CIとCDは手法としても重なる所がある
- **CIからCDへ**と連続したプロセスとして組み立てられる
上記の観点からCI/CDとまとめられて語られる事が多い。


### 1-1. CI

**CI: Continuous Integration(継続的インテグレーション)**

- インテグレーション = 統合
  - ソフトウェア開発においては、「ソフトウェアのコードの統合」を指す

- コードの統合とは
  - 「メインブランチにコードをマージする」こと
コードをマージしてもソフトウェアが「ビルドできること」、「意図した通りに動くこと」を検証する必要がある。多くの現場では複数の開発者が同時並行で開発をしているため、複数のブランチのコードを再数的には統合する必要がある。

**CIは、上記のような開発環境におけるコードの統合を継続的に実現するための手法である**。

### 1-2. CD

**CD: Continuous Delivery(継続的デリバリー) or Continuous Deployment(継続的デプロイメント)**

- デリバリー ≒ デプロイメント
  - 同じだったり違かったりのよう
  - デリバリー = 価値を届けるという意味が良さそう。

- 価値を届けるとは
  - メインブランチにコードがマージされ、自動テストもパスし、いつでもリリース可能(利用可能)な状態にする
  - 本番にデプロイし、ユーザが新しい機能を使えるようにする

**CDは、上記のような「価値を届ける」ことを継続的に実現するための手法である**。

## 1-3. なぜCI/CDが重要なのか？

- ビジネスで求められるもの

1. 市場における競争力の維持
2. 市場の変化に対応すること
3. 新しい市場を探す

ソフトウェア開発において上記のような要求を満たすには、**何度も「開発・統合・デリバリー」を繰り返して市場からのフィードバックを受け取り、ソフトウェアを改善し続ける必要がある**。

「開発・統合・デリバリー」のサイクルを高頻度かつ継続的に回すための仕組みとなるのがCI/CDであり、だからこそCI/CDが重要視される。

## 1-4. CI/CDを実際にやってみる

[GitHub CI/CD チュートリアル: 継続的インテグレーションのセットアップ](https://circleci.com/ja/blog/setting-up-continuous-integration-with-github/)

既存のリポジトリにディレクトリ作成してはだめだった。
リポジトリ1個につき、プロジェクト1個？
新しくリポジトリ作成したら無事GitHubとCircleCIを連携できた。

- 大まかな流れ

1. pythonアプリをセットアップ
2. テストを作成
3. CircleCIの設定ファイルを作成(`.circleci/config.yml`)
4. コードベースをGitHubにプッシュ
5. 作成したGitHubリポジトリとCircleCIの接続を確認

- 違う記事でもやってみる
  - CircleCIでHello World

```yml: .circle/config.yml
version: 2.1
jobs:
  build:
    docker:
      - image: circleci/node:4.8.2
    steps:
      - checkout
      - run: echo "hello world"
```

1. `circleci/node:4.8.2`というイメージを利用したDocker環境を立ち上げ
2. CircleCIがGitHubリポジトリをチェックアウトして上記Docker環境にリポジトリをクローン
3. `echo "hello world"
4. 新規リポジトリにプッシュし、CircleCIでリポジトリを連携させる
5. 自動ビルド？
6. 詳細を見てみると`echo "hello world"が実行されている。

つまり、CircleCIとリポジトリを連携させると、自動でテストされる事が分かった。

## 1-5. CI/CDのフロー

1. ソースコードがGitへコミットされるとCIによって自動的に各種テストが行われる
「コードにエラーがないか」、「既存の機能を破壊してないか」
テスト結果は開発者に送られる。

2. 次にCDによってコードがブランチにマージされ、ビルドが行われる
CDによってビルドされたアプリケーションは、自動でテスト用のサーバにデリバリーされる。

[CI/CDのパイプラインのイメージ](https://pfs.nifcloud.com/navi/words/images/ci_cd.png)


## 2. DevOps

参考:
[DevOps](https://web.archive.org/web/20220615100343/https://ja.wikipedia.org/wiki/DevOps)
[DevOps とは?](https://aws.amazon.com/jp/devops/what-is-devops/)


- DevOpsとは
ソフトウェア開発手法の一つ。
開発(**Dev**elopment)と運用(**Op**eration**s**)を組み合わせた**かばん語**(合成語)で、開発担当者と運用担当者が連携して協力する開発手法を指す。(狙いとしては両担当者の境目もあいまいにする)
ソフトウェアを迅速にビルドおよびテストする文化と環境により、確実なリリースを以前よりも迅速に高い頻度で可能とする**組織体制の構築**を目指す。

### 2-1. DevOpsを行うメリット

1. 企業は顧客により良いサービスを提供し、**市場競争力を高める**ことができる。
   1. 例えば、マイクロサービスと継続的デリバリーによって更新をしばやくリリースできる。
   2. リリースの頻度とペースが上がることで、製品の革新と改善をより迅速化できる。よりすばやく新しい機能のリリースやバグの修正を行うことができ、競争優位性を高められる。

2. 開発と運用の境目をあいまい、または1つのチームに統合することで、エンジニアはアプリケーションのライフサイクル全体にわたって作業するため、**幅広くスキルを磨くことができる**。
多くの責任を共有する。開発と運用間の引き渡しにかかる時間の短縮。

3. 自動化によるリスク軽減
複雑なシステムまたは変化するシステムを効率的に管理し、リスクを減らすために役立つ。

4. 制御を保持してコンプライアンスを遵守しながらすばやく移行できる
セキュリティを保ちながらDevOpsモデルを導入できる。

### 2-2. 具体的なイメージ

1. 手動で時間がかかっていた処理を**自動化する手法を使用**する。
2. 迅速かつ確実にアプリケーションを運用して展開するために役立つ**テクノロジースタックとツールを使用する**。

### 2-3. キーワード

- **CI(継続的イングレーション)**

- **CD(継続的デリバリー)**

- **マイクロサービス**

> マイクロサービスのアーキテクチャは、1 つのアプリケーションを小さなサービスのセットとして構築するためのアプローチとして設計されています。各サービスは独自のプロセスで実行され、軽量のメカニズムで明確に定義されたインターフェイスによって他のサービスと通信します。通常は HTTP ベースのアプリケーションプログラミングインターフェイス (API) を使用します。マイクロサービスはビジネスコンピューティングを中心に構築され、各サービスは 1 つの目的に範囲が限定されています。さまざまなフレームワークやプログラミング言語を使用してマイクロサービスを作成し、単一のサービスまたはサービスのグループとして、それらを単独でデプロイできます。

- **Infrastructure as Code**

> Infrastructure as Code は、バージョン管理や継続的インテグレーションなど、コードおよびソフトウェア開発技術を使用して、プロビジョンおよび管理されたインフラストラクチャの手法です。クラウドの API によるモデルでは、開発者とシステム管理者がプログラムでスケールに応じてインフラストラクチャを操作できます。手動でリソースをセットアップして設定する必要はありません。そのため、エンジニアはコードベースのツールを使用してインフラストラクチャを操作でき、アプリケーションコードと同じ方法でインフラストラクチャを扱えます。コードで定義されるため、インフラストラクチャとサーバーは標準化されたパターンですばやくデプロイされ、最新のパッチまたはバージョンで更新され、反復可能な方法で複製されます。

- **モニタリングとロギング**

> 組織は、メトリクスとログをモニタリングし、アプリケーションおよびインフラストラクチャのパフォーマンスが製品のエンドユーザーエクスペリエンスにどのように影響しているかを確認できます。アプリケーションおよびインフラストラクチャで生成されたデータとログの取り込み、分類、および分析によって、組織は、問題または予期しない変更の根底にある原因を捉えながら、変更や更新がどのようにユーザーに影響するかを理解できます。サービスが 24 時間年中無休で使用できるように求められるにつれて、またアプリケーションとインフラストラクチャの更新頻度が増大するにつれて、アクティブモニタリングはますます重要になっています。アラートを作成してデータのリアルタイム分析を実行することも、組織がより積極的にサービスをモニタリングするために役立ちます。

- **コミュニケーションと共同作業**

> 組織におけるコミュニケーションと共同作業の向上は、DevOps の主な文化的側面の 1 つです。DevOps のツールとソフトウェア配信プロセスのオートメーションを使用すると、開発および運用に対するワークフローおよび責任を物理的に一緒に担うことになるため、共同作業が定着します。それに加えて、これらのチームは、チャットアプリケーション、課題やプロジェクトの追跡システム、および wiki の使用を通して、情報共有やコミュニケーションの促進について強力な文化的基準を定めます。これにより、開発者、運用、およびマーケティングや営業など他のチームの全体にわたりコミュニケーションがスピードアップします。組織のあらゆる部分が目標とプロジェクトに向かってより緊密に連携します。

## 3. DevOpsツール

DevOpsライフサイクルの主要フェーズ

1. 発見しよう
2. 計画する
3. ビルド
4. テスト
5. 監視
6. 運用
7. 継続的なフィードバック

これらのDevOpsライフサイクルを支援するツールを調べる。

### 3-1. 発見しよう

発見のフェーズでは、DevOpsチームはプロジェクトのスコープを調査して定義する。このフェーズでは以下のツールなどを使用し、ソフトウェアチーム全体がアイデアを集めて調査を行えるようになる。

- Jira Product Discovery
  - 製品管理
  - 新しい製品アイデアの優先順位づけ
- miro
  - オンラインホワイトボードサービス
  - リモートや対面での会議において、チームでの共同作業を活性化する
- Mural
  - こちらもホワイトボードツール

### 3-2. 計画する

スピードと品質を向上させるために採用する手法

1. アジャイルプラクティス
アジャイルハンドブックをお手本に、開発チームと運用チームが作業を小さく管理しやすいチャンク(塊)に分割し、より迅速にデプロイできるようにする。

2. もう1つのプラクティス
ユーザのフィードバックを継続的に収集し、それを実用的なインプットにまとめ、開発チームのためにそれらのアクションに優先順位を付ける。

- Jira Software
  - タスク管理用
- Confluence
  - チームのワークスペース
  - 情報共有
- slack
  - メッセージアプリ
  - IT企業に導入傾向が強い

### 3-3. ビルド

#### 3-3-1. 本番環境と同一の開発環境

自分のマシンでは動作していても、他の人のマシンで動かない事は往々にしてある。
チームメンバーで同一の方法で環境を構築する事が大事。

- Kubernetes
  - k8s または、Kubeと呼ばれる。
  - OSS
  - コンテナの運用管理やスケールを支援する
> Kubernetesを活用することによって、コンテナ化されたアプリケーションのデプロイ等の手動プロセスを無くし、Docker コンテナのホストを全てクラスタ化実行を実現させたり、負荷がかかった際にスケーリングを行ったり、冗長化の仕組みを行うことさせも可能になります。

- Docker
  - Docker社が開発
  - コンテナ型の仮想環境を作成、配布、実行するためのプラットフォーム

#### 3-3-2. コードとしてのインフラストラクチャ

**OS・ミドルウェアといったITインフラ構築・運用をコード化すること**を指す。
Infrastructure as codeで自動する事で、インフラ構築・運用の人為的ミス、工数の増加、コストの増加を防ぐことができる。

- Ansible
  - Simple, Powerful, Agentlessの3つの特徴を掲げる
  - Python製のインフラ構築自動化ツール

- CHEF
  - OSS
  - インフラにおけるサーバ構成管理や、サーバへのファイル展開作業(プロビジョニング)を自動化する

- Docker

- Puppet
  - OSS
  - OS設定やアプリケーションの構築を自動化する

- Terraform
  - OSS
  - golangで開発
  - インフラの自動構築ツール
  - インフラの構成をソースコードとして管理できる

#### 3-3-3. ソース管理とコラボレーションコーディング

**コードのソース管理の重要性**
コードのソース管理を行うことで、すべての変更の確認の共有が行え、より簡単にコラボレーションできる。プルリクエストを介してピアレビュー(同僚・仲間とレビューしあう)を行うことによって、コードの品質とスループットを向上できる。
**プルリクエスト**: リポジトリ内の開発ブランチにプッシュした変更についてチームに伝えるもの。

- Bitbucket
  - チーム開発用Gitソリューション
  - ATLASSIANから提供
    - SourceTreeもATLASSIAN社のサービスなので相性が良い　
  - 無料枠でプライベートリポジトリが作成できる

- GitHub
  - データ保存だけでなく、自分以外のエンジニアとの共有や、誰が・どこを・いつ編集したのかの管理を簡単に行える
  - 無料枠で公開・共有が前提のリポジトリが利用できる

- GitLab
  - GitHubにインスパイヤされて作られた
  - Issue(課題)の管理、コードレビュー、CI/CDをひとつの画面で行うための統一的な機能を提供する


#### 3-3-4. 継続的デリバリー

共有リポジトリにコードを1日に数回チェックインして、その都度テストするプラクティス。
問題を自動で早期検出して、最も修正しやすいときに修正でき、できるだけ早くユーザに新機能を提供できる。
プルリクエストによるコードレビューにはブランチの作成が必要だが、この方法は大流行している。

- Circleci
- Bitbucket

### 3-4. テスト

#### 3-4-1. 自動テスト

テストツールは、ニーズと機能に対応してさまざまなものがある。
DevOpsでは自動化は不可欠な機能。長期的に見れば投資に見合う価値がある。

- Zephyr Squad
  - Jira(Atlassianが提供するチケット管理ツール)内のアジャイルチーム向けのテスト管理
  - 具体的には、基本的なテストの設計と実行、自動化とBDDおよびCIツールとの統合、単一プロジェクトのレポートといった基本的な機能を提供する

- snyk(スニーク)
  - コードやオープンソースとその依存関係、コンテナやIaCにおける脆弱性の発見、優先順位を付けて自動的に修正する。

#### 3-4-2. デプロイ

ソフトウェアのリリースで最もストレスが大きい部分の1つは、今後のリリースのためにすべての変更、テスト、デプロイの情報を1ヶ所にまとめること。リリース前位に状況報告のための長いミーティングをしないためにもリリースダッシュボードが活用される。

- Jira Software
  - デプロイダッシュボード

#### 3-5-3. デプロイの自動化

自動デプロイの魔法のレシピはないが、広く採用されているのはRubyまたはbashをしようして運用のランブックをcmd実行可能スクリプトに変換すること。

- Bitbucket

- AWS CodePipeline
  - 完全マネージド型の継続的デリバリーサービス

### 3-5. 監視

**アプリケーションとサーバのパフォーマンス監視**

自動化する必要がある監視には、サーバ監視とアプリケーションのパフォーマンス監視の2種類がある。

- AppDynamics
  - リアルタイムでユーザやアプリケーションのパフォーマンスを監視および管理する

- Splunk
  - あらゆるインフラやアプリケーション機器を対象にした総合的なログ分析を行う

### 3-6. 運用

**インシデント、変更、問題の追跡**

DevOpsチーム間のコラボレーションを円滑にする鍵は、全員が確実に同じ作業を見るようにすること。インシデントとソフトウェア開発プロジェクトを異なるシステムで追跡することほど、開発と運用のコラボレーションの妨げになるものはない。
問題を迅速に特定して修正できるように、インシデント、変更、問題、ソフトウェアプロジェクトを1つのプラットフォームにまとめるツールを使用する。

- Jira Software

- Opsgenie
  - 重要なアラートを見逃さず、サービスを回復し、根本的な問題を修正する

### 3-7. 継続的なフィードバック

構築した製品が適切なものかどうか、届いた顧客の意見に耳を傾けることが大切。継続的なフィードバックには、**定期的なフィードバックを収集するための文化やプロセス**に加えて、**フィードバックからインサイトを引き出すためのツール**が含まれる。

- slack
  - チャットツールをお気に入りのアンケートプラットフォームと統合する

- pendo
  - ノーコードで使える分析・ガイド・フィードバックの3つの機能を備え、統合利用することで、ソフトウェアの定着化とユーザ体験の向上を支援する

## 3-8. 結論

> 開発チーム・運用チームが使用したいと思うツールとの統合に対応したDebOpsツールチェーンを用意することが重要。
適切なツールの導入・使用が大事。
