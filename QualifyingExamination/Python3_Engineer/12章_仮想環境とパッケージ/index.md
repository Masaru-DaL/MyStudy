# 12章 仮想環境とパッケージ
出題数 1問

## 環境の管理
#### 環境構築
- Pythonのインストール(Mac, Windows)
- VScode(Editor)のインストール
が主な所になってきます。

#### 仮想環境の生成: venv(旧称: pyvenv)
- Good Point
  - Python公式の管理ツール
  - パッケージの切り替えをアプリケーション毎に出来る
- Bad Point
  - バージョンの切り替えは出来ない

:::message
最近は`pyenv(not venv)`でバージョン管理し、`poetry`でライブラリ管理するケースが増えている。
:::

##### pyenvとは
- **Pythonのバージョン管理が可能な仮想環境**
- 2系と3系で環境を切り替えられる
- プロジェクト毎に環境を切り替える事が簡単に出来る

:::message alert
Qiitaですが、便利だからとりあえずpyenv使おうっていう考えはあまり良くないようです。
[pyenvが必要かどうかフローチャート](https://qiita.com/shibukawa/items/0daab479a2fd2cb8a0e7)

要はメリット・デメリットを把握した上できちんと使いましょうということです。
:::

##### poetryとは
- Pythonのパッケージマネージャー
  - パッケージ管理ファイルの生成・変更
  - インストールされているパッケージのアップデート
  - プロジェクト毎の仮想環境のセットアップ
  - などなど...

:::message
他の言語にある`npm`, `yarn`などと同様のパッケージマネージャーでまだまだ新しいようです。

参考(記事が一年前なので現在はどうかという所ですが): [Poetryをサクッと使い始めてみる](https://qiita.com/ksato9700/items/b893cf1db83605898d8a)
:::

#### pipによるパッケージ管理
**パッケージをインストールしたり、削除したりする**
- poetryでパッケージ管理していても、pipを使う場合がある

##### pipのコマンド
- Install
  - `pip install パッケージ名`
- Uninstall
  - `pip uninstall パッケージ名`
- Version Designation
  - `pip install パッケージ名=バージョン`
- Upgrade
  - `pip install -upgrade パッケージ名`
- Version Information
  - `pip show パッケージ名`
- Show Package List(install済)
  - `pip list`
- All Package Install
  - `pip install -r requirements.txt`
- Create requirements.txt
  - `pip freeze > requirements.txt`


