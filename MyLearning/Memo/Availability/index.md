# 可用性とは

## 1. キーワード

* [x] 可用性
* [ ] aws
* [x] システム
* [ ] s3
* [ ] ec2
* [ ] 意味
* [ ] 分かりやすく
* [x] 英語 読み方
* [ ] 可用性ゾーン
* [ ] アベイラビリティゾーン
* [ ] 可用性セット

* 予備キーワード
1. 可用性 完全性 機密性
2. 可用性 信頼性 保守性
3. 信頼性 保守性
4. 非機能要件
5. クラウド

* 可用性と信頼性
https://bcblog.sios.jp/what-is-availability/

* RASの深掘り
  + 耐障害性システムになると高価になる

* 可用性を高める2つの方法
  + より可用性の高いシステムへリプレイスする
  + 同じシステムを呼びとして別途用意しておく(=冗長化)

[オンプレミスの可用性](https://www.google.com/search?q=%E3%82%AA%E3%83%B3%E3%83%97%E3%83%AC%E3%80%80%E5%8F%AF%E7%94%A8%E6%80%A7&sxsrf=ALiCzsYgnOYdf0DYcNeLbQe92YmGQ0QAuQ%3A1666656080747&ei=UCdXY4qWLY7i2roPodORgAk&ved=0ahUKEwiK_p7difr6AhUOsVYBHaFpBJAQ4dUDCA8&uact=5&oq=%E3%82%AA%E3%83%B3%E3%83%97%E3%83%AC%E3%80%80%E5%8F%AF%E7%94%A8%E6%80%A7&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEAQQgAQQJToKCAAQRxDWBBCwAzoNCAAQ5AIQ1gQQsAMYAToFCAAQogQ6BwgAEB4QogQ6BAgAEB5KBAhNGAFKBAhBGABKBAhGGAFQQljvFmDBGGgBcAF4AIABcogBkAOSAQMyLjKYAQCgAQHIAQ_AAQHaAQYIARABGAk&sclient=gws-wiz)

* オンプレ/クラウドで可用性へのアプローチはどう変わるか
  + [物理から仮想へ](https://www.google.com/search?q=%E7%89%A9%E7%90%86+%E4%BB%AE%E6%83%B3+%E7%A7%BB%E8%A1%8C+%E5%8F%AF%E7%94%A8%E6%80%A7&oq=%E7%89%A9%E7%90%86%E3%80%80%E4%BB%AE%E6%83%B3%E3%80%80%E7%A7%BB%E8%A1%8C%E3%80%80%E5%8F%AF%E7%94%A8%E6%80%A7&aqs=chrome..69i57.9509j0j1&sourceid=chrome&ie=UTF-8)
    - 基本的アプローチは変わらない
    - ここを詳しく調べる
サーバを物理から仮想へリプレイスした図を作る。(集約)
仮想化のリスクが分かる図を作る(障害発生時)

* クラウド(laaS)
  + [IaaS PasS SaaS](https://www.google.com/search?q=IaaS+PasS+SaaS&sxsrf=ALiCzsYWFP-7U2iqRPKvL02acIWsZv1Bag%3A1666655588361&ei=ZCVXY5vWFZWk2roPxd6g-Ag&ved=0ahUKEwibmLryh_r6AhUVklYBHUUvCI8Q4dUDCA8&uact=5&oq=IaaS+PasS+SaaS&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEIMBEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6CggAEEcQ1gQQsAM6CwgAEIAEELEDEIMBOgUIABCABDoECAAQQzoNCAAQgAQQsQMQgwEQDToHCAAQgAQQDUoECE0YAUoECEEYAEoECEYYAFCsOFjmhAFg54YBaApwAHgAgAHCAYgBig6SAQM3LjmYAQCgAQHIAQrAAQE&sclient=gws-wiz)

SLAについて。
クラウドベンダーが担保する範囲を定めたもの。

* AWS
AWSが担保してくれる範囲
ユーザが気にする範囲
  + キーワード
  + アベイラビリティゾーン
  -
