# Python csv基礎

この記事ではPythonのcsvについて解説します。

Pythonのcsvモジュールを操作は、アプリケーションから取り出したcsvファイルを使って独自の集計やデータの移行などさまざまな場所で活用することができます。

## csvとは

Pythonのcsvは、CSV（**C**omma **S**eparated **V**alues）形式で書かれたファイルを扱えるモジュールのことを指します。csvを使用する際は`import`が必要です。

CSVファイルはスプレッドシートやデータベース間で使用される最も一般的な形式です。Excelファイルと混同されがちですが、CSVファイルの方が**互換性が高い**という特徴があります。

以下がCSVファイル形式で書いた場合です。

```csv:
学校名, 学年, 名前, 専攻カリキュラム, 成績
Envader, 1st, Bob, Programming, A
Envader, 2nd, Alisa, UI/UX, B
Envader, 1st, Mike, Programming, B
Envader, 2nd, Adam, DataScience, S
Envader, 2nd, Lisa, Front-end, A
```

上記のCSVファイルを読み込むと以下のようになります。

![](2022-11-13-06-15-03.png)

## ファイル操作

csvモジュールはCSVファイルを扱いますので、まず簡単にPythonにおけるファイルの取り扱いを説明します。

- with
`with`はファイルを**一定期間操作する構文**です。`with`には、ファイルを自動でクローズするという特徴があります。Pythonのファイル操作には`open()`関数がありますが、こちらはファイルを明示的にクローズする必要があります。本記事では`with`を使ってファイル操作を行います。

withの構文は以下です。

```python:
with open(<ファイル>, mode=<"モード">, encoding="文字コード") as <別名>:
```

ファイル指定は必須です。モードと文字コードは必要に応じて使用・使い分けします。また、`as`でファイル操作を行うファイルオブジェクトに別名を付けることができます。その別名はファイルをクローズするまでのスコープで使用できます。

モードはいくつかの種類とそれぞれの特徴がありますので表にまとめました。

| mode=” “ | 詳細 | 特徴 |
| --- | --- | --- |
| r | 読み込み用 | デフォルト値 |
| w | 書き込み用 |  |
| x | 新規作成 + 書き込み用 | 既にファイルがあるとエラーになる |
| a | 追記用 |  |
| b | バイナリモード | r, w, aと一緒に指定が必要 |
| t | テキストモード | r, w, aと一緒に指定が必要 |
| + | 更新用 | r, w, a, xと一緒に指定が必要 |

## csvモジュールの主な関数

今回紹介するcsvモジュールの関数を表にまとめました。

| 関数 | 詳細 | 特徴 |
| --- | --- | --- |
| csv.reader | ファイルの読み込み | リスト型を返す |
| csv.Dictreader | ファイルの読み込み | 辞書型を返す |
| csv.writer | ファイルの書き込み | リスト型を書き込む |
| csv.DictWriter | ファイルの書き込み | 辞書型を書き込む |

## CSVファイルの読み込み

ここから、実際にcsvモジュールを使ってCSVファイルを操作していきます。まずはCSVファイルの読み込み操作から行います。

### csv.reader

CSVファイルの読み込みは、`csv.reader`を使用します。

- csv.readerの基本的な使い方

以下のCSVファイル（`sample.csv`とします）を読み込みます。

```csv:
学校名, 学年, 名前, 専攻カリキュラム, 成績
Envader, 1st, Bob, Programming, A
Envader, 2nd, Alisa, UI/UX, B
```

```py:
import csv

with open("sample.csv") as rf:
    reader_object = csv.reader(rf)
    # ①
    print(reader_object)

    # ②
    for row in reader_object:
        print(row)

# 出力結果①: <_csv.reader object at 0x1029fc040>

# 出力結果②:
# ['学校名', ' 学年', ' 名前', ' 専攻カリキュラム', ' 成績']
# ['Envader', ' 1st', ' Bob', ' Programming', ' A']
# ['Envader', ' 2nd', ' Alisa', ' UI/UX', ' B']
```

出力結果①は、`open()`で開いたファイルオブジェクトを`csv.reader()`に渡して出力した結果です。つまり、`csv.reader`でファイルオブジェクトを読み込むと`reader`オブジェクトが返されます。

csv.readerが返したreaderオブジェクトはイテレータプロトコルに対応します。そのため、②のようにfor文で行ごとに取り出すことができます。


- 行ごとのデータの取り出し
    - `csv.reader`オブジェクトはイテレータとみなせること
    - for文を使用する
- 二次元配列として取得する
    - リスト内包表記を使用する
- 行・列・要素の取得
    - 行の取得方法
    - 要素の取得方法
    - 列の取得方法（転置を行う）
- 文字列を数値に変換
    - デフォルトで各要素が文字列であること
    - 型変換を行う必要があること
- 区切り文字を指定
    - デフォルトが`,`（カンマ）であること
    - 任意の区切り文字の指定方法
- 引用符の扱い
    - 引数`quoting`の使い方
- 改行を含むファイルの場合
    - ファイル操作の時点で `newline = ‘’`としておくほうが安全
    - pythonドキュメントを引用する
- headerなどを含むファイルの場合
    - リスト内包表記で取り出す際にスライスと組み合わせる方法があることを説明する
    - 後述するpandasを使う方が楽だということも伝えるので上はさらっと

### csv.DictReader

- 基本的な使い方
- OrderedDictに触れる
- headerがない場合は`fieldnames`を使用する
- headerの削除方法
    - `pop()`を使用する
    - `popitem()`, `del`で出来ることをさらっと紹介

## csvモジュールを使った書き込み

### csv.writer

- 基本的な使い方
    - `writerow()`
    - `writerows()`
- 区切り文字の指定
- 引用符の扱い
- 改行を含むファイルの場合
- headerなどを加える場合

### csv.DictWriter

- 基本的な使い方
    - `writerow()`
    - `writerows()`
- キーが存在しない場合の`extrasaction`の使い方
    - `extrasaction`のデフォルトが`’raise’`であること

## まとめ

まとめ
