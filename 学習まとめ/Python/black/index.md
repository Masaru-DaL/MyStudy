# black とは何か

参考: [もう Python の細かい書き方で議論しない。black で自動フォーマットしよう](https://blog.hirokiky.org/entry/2019/06/03/202745)

1. python のコードフォーマッター
2. 自動的に Python プログラムの書き方を修正してくれる
3. PEP8 のコード規約に準拠したフォーマッター
4. 制限が多く、他人数で python のコードを書く際に統一された書き方ができる(メリット)

:::message
特徴をまとめると、
black は自動フォーマッターというよりも制限のきつい PEP8 であるということのようです。
:::

## 1. black の install

適用させたいのは VScode です。
拡張機能に Black Fomatter というのがありますが、今回は使用しません。
また、Mac 環境で進めていきます。

pip、もしくは brew でインストールを行います。
`pip3 install black`
`brew install black`
どちらかお好きな方でインストールします。

## 2. VScode のセットアップ

- ゴールは VScode で保存した際に自動で適用されること。
  `setting.json`に追加する内容を書いていきます。
  ※GUI で設定することも出来ます。

#### 2-1. black を適用させる

1. `"python.formatting.provider": "black",`
   python のフォーマッターを black に設定する

2. `"python.formatting.blackPath": "/opt/homebrew/bin/black"`
   `which black`で black を使用する際のフルパスをチェックし、記述します。
   パスは各個人で違うと思われます。

#### 2-2. 保存した際に自動フォーマット

`"editor.formatOnSave": true,`

#### 2-3. python ファイルのみに適用させる

```json: setting.json
"[python]": {
    "editor.defaultFormatter": null,
  },
```

Prettier をデフォルトのフォーマッターとして設定している場合に必要になります。
(Prettier は Python コードのフォーマットには対応していません)

#### 2-4. 試してみる

保存しても適用されません...
大体の記事を漁ってもこれ以上の情報が出てきません。

結局の原因は linter でした。

## 3. linter

:::message
linter とは、**コードに問題点がないかを確認する静的解析ツール**のことです。
ある記事には`pylint`がデフォルトで走るようになっているという事が書いてありました。
:::

#### 3-1. linter の設定

`"python.linting.enabled": true`
こちらを setting.json に記述すると...

無事保存した時に自動でフォーマットされました。

## 4. setting.json

最終的に black 用で設定する`setting.json`は以下の通り

```json: setting.json
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackPath": "/opt/homebrew/bin/black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": null,
  },
```
