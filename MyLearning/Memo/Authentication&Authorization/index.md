# 認証と認可の違いについて、各記事をまとめる

## 要件

タイトル: 認証認可の違いとは
全記事を読む
いいところを全部持ってくる

引用はギットハブなどのいいところから引用する

キーワード
* 認証
* 認可
* 違い
* oauth
* アカウンティング
* 承認
* アクセス制御
* とは
* Saml
* Aws
* Id
* 意味
* 例え

## 1. [認証と認可の違いとは｜セキュリティの強化について説明](https://solution.kamome-e.com/blog-security-20211021/#:~:text=%E3%80%8C%E8%AA%8D%E8%A8%BC%E3%80%8D%E3%81%A8%E3%80%8C%E8%AA%8D%E5%8F%AF%E3%80%8D%E3%81%AF%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%81%A7%E3%82%82%E8%8B%B1%E8%AA%9E, %E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E5%BF%85%E8%A6%81%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82)

* 認証
  + 相手が「誰であるのか」を確認、特定すること
  + **サーバ**が、ユーザから入力されたID, PASSWORDを受け取り、本人かどうかを確認する。
    - 認証が成功すれば本人だと特定し、認証が失敗すれば認証失敗となる
  + AuthN

* 認証情報
1. 知識情報: パスワード認証など
2. 生体情報: 顔認証
3. 所持情報: SMS認証
この内2つ以上で認証すること -> 多要素認証

* 認可
  + 分かりづらい
  + 対象物を利用可能にする権限を与えること
  + 認可という過程を経て、サービスを扱えるようになる
  + **サービス**が(認可)与える
  + AuthZ

* 認証と認可が分かれていなかった場合
  + 認証だけの場合
    - 全ての人に全ての権限が付与される
    - 管理者権限が誰でも使えるようになると考えるとどうなるかはご想像の通りです。
  + 認可だけだった場合
    - パスワードがないという事です。
    - 自分だけのアカウントという概念がなくなり、なりすましが行えてしまうということが想像できますよね

認証は**本人確認**
認可は**アクセス権限の付与**

## 2. [認証と認可の違いを分かりやすくまとめてみる](https://zenn.dev/tanaka_takeru/articles/aecd36a805886d)

* 認証
  + What you are
    - 生体認証
  + What you have
    - 所持情報
  + What you know
    - 知識情報

* 認証と認可を同時に行うのが望ましい
  + 免許証
    - 顔写真付きで本人確認が行える: 認証
    - 持っている事で自動車に乗ることを許可される: 認可

authだけで認証という意味でもあるからややこしい。

## 3. [認証と認可の違いとは？ゼロトラストのためのアクセス制御の実現](https://www.stylez.co.jp/zerotrust_columns/what_is_the_difference_between_certification_and_authorization/)

## 4. [Webサイトに必要な認証・認可とは？意味や違いを含めて解説](https://www.customer-data-cloud.com/blog/what-is-neccesary-certification-of-web-sight)

1. Webサービスの**管理者がサービスにアクセスできる条件を定めます**。
2. 条件の一覧は、アクセスコントロールリスト（ACL）と呼ばれ、ネットワークルータを通過するタイミングで、**コンピュータがこのリストに基づき自動的にユーザを判別します**。
3. リスト上の条件をすべて満たしたユーザは、**アクセス許可を得て**、Webサービスにログインできるようになります。

* 認証の役割
  + 本人であることを確認する。
  + なりすまし、ハッキングなどの防止
* 認可の役割
  + その人がどういった権限を持っているかを確認する
  + サービスの適切な運用のため

## 5. [認可](https://e-words.jp/w/%E8%AA%8D%E5%8F%AF.html)

> 本来、認証と認可は別の過程であり、認証を経ずに特定の条件を指定して認可のみを行うこともできる。しかし、単純なシステムでは認証と同時に認可も済んでしまうことも多く、字面も似ており、日常的な語彙としては似た意味合いであるため、しばしば混同される。認証向けの技術を認可に用いるといった不適切な事例も起きている。

> 英語でも “authentication” と “authorization” は日常語彙としては意味も綴りも似ており、日本語の場合と事情は近い。さらに、方式名や製品名に使用する際などに、どちらも “auth” と略されることがあるため、余計に混同しやすいという事情があり、近年では認証を “authn” 、認可を “authz” として別の略号を用いることが提唱されている。

***

## 認可

https://e-words.jp/w/%E8%AA%8D%E5%8F%AF.html#:~:text=%E8%AA%8D%E5%8F%AF%E3%81%A8%E3%81%AF%E3%80%81%E3%81%82%E3%82%8B%E8%A1%8C%E7%82%BA, %E3%82%92%E6%8C%87%E3%81%99%E3%81%93%E3%81%A8%E3%81%8C%E5%A4%9A%E3%81%84%E3%80%82

* ある行為などをしても良いと認めること
  + コンピュータシステムの利用者に特定の操作権限を付与する処理や手続を指すことが多い

https://qiita.com/kaysquare1231/items/c4e4736f2a924b03777b#%E8%AA%8D%E5%8F%AF-1

レンタカーを借りる際に、免許証の提示を求められた
学生割引を受ける際に、学生証の提示を求められた
