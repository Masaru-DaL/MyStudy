# データベースの正規化とは

## 1. 正規化とは

[関係の正規化](https://ja.wikipedia.org/wiki/%E9%96%A2%E4%BF%82%E3%81%AE%E6%AD%A3%E8%A6%8F%E5%8C%96)

> 関係の正規化（かんけいのせいきか）は、関係データベース (リレーショナル・データベース) において、関係（リレーション）を正規形と呼ばれる形式に準拠させることにより、データの一貫性の維持と効率的なデータアクセスを可能にする関係設計を導くための方法である。正規形には様々なものが存在するが、いずれにせよ、正規化を行うことにより、データの冗長性と不整合が起きる機会を減らすことができる。

- 関係の正規化の定義
**関係(リレーション)を正規形と呼ばれる形式に準拠させること**
※正規形には様々なものが存在する

- 関係の正規化とは
データの一貫性の維持と効率的なデータアクセスを可能にする関係設計を導く。

- 正規化を行うことによるメリット
データの冗長性と不整合が起きる機会を減らせる。

> 多くの関係データベース管理システム (RDBMS) は、論理的なデータベース設計とデータを格納する物理的な実装方法とが十分に分離されていないので、完全に正規化されたデータベースへのクエリ（検索質問）はパフォーマンスが良くないことがある。このような場合、パフォーマンスを向上させるためにデータの一貫性の低下と引き換えにあえて非正規化されることもある。

- 非正規化を行う場合もある

## 2. もう少し正規化について詳しく

[データベースの正規化の基礎](https://learn.microsoft.com/ja-jp/office/troubleshoot/access/database-normalization-description)

> 冗長なデータがあると、ディスク領域が浪費され、保守上の問題点が生じます。 複数の場所に存在するデータの変更が必要な場合、すべての場所でそれらのデータがまったく同一になるように変更する必要があります。 顧客の住所を変更する際に、データが格納されているのが "顧客" テーブルのみで、データベース内の他のテーブルに存在しない場合、変更作業を簡単に行うことができます。

- 正規化をしなかった場合、つまり冗長なデータがあった場合

1. ディスク領域が浪費され、保守上の問題点が生じる。
2. 複数箇所に存在するデータの変更の必要性が生じた場合、その全てを変更しなくてはならない。

> データベースの正規化にはいくつかの規則があります。 各ルールは"通常の形式" と呼ばれます。最初の規則が観察された場合、データベースは "最初の通常の形式" と呼ばれます。最初の 3 つの規則が観察された場合、データベースは "3 番目の通常の形式" と見なされます。他のレベルの正規化は可能ですが、3 番目の標準形式は、ほとんどのアプリケーションに必要な最高レベルと見なされます。

- 正規化にはいくつかの規則がある。
  - 各ルールは「通常の形式」と呼ばれる
    - あまり聞いたことがない
    - 第◯正規化というものがある、程度で良さそう
  - 第3正規化が良い感じ

> 多くの規則や規格がそうであるように、現実のシナリオは常に規則に完全に適合しているとは限りません。 一般的に、正規化を行うと追加テーブルが必要となるため、わずらわしいと感じる顧客もいます。 正規化の最初の 3 つの規則のいずれかに違反した設計をする場合、冗長データや矛盾する従属関係など、アプリケーションで発生する可能性のある問題点を考慮しておく必要があります。

- 正規化を行うと追加テーブルが必要となる

## 3. 正規化の例

[データベースの正規化の基礎](https://learn.microsoft.com/ja-jp/office/troubleshoot/access/database-normalization-description)を参考にしながら、自分で実際にデータベースとテーブルを作成して行ってみる。
使用先 -> [Envader](https://envader.plus/)

[正規化における時点の名前](https://breezegroup.co.jp/wp-content/uploads/2020/04/%E6%AD%A3%E8%A6%8F%E5%8C%96%E3%81%AE%E7%A8%AE%E9%A1%9E-1-1024x275.png)で、何となくイメージは掴んでおく。

### 3-1. 非正規系

- 正規化される前のテーブルを作成する。

1. データベースの作成(normalize_dbとしてデータベースを作成する)

```sql:
mysql> create database normalize_db;
Query OK, 1 row affected (0.06 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| food_app           |
| information_schema |
| mysql              |
| normalize_db       |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.01 sec)

mysql> use normalize_db;
Database changed
```

2. tableの作成(results_sheetとしてテーブルを作成する)

```sql;
mysql> create table normalize_db.results_sheet (
    -> id int,
    -> student_code int,
    -> student_name varchar(10),
    -> subject_code varchar(10),
    -> subject_name varchar(10),
    -> academic_year int,
    -> results varchar(5));
Query OK, 0 rows affected (0.11 sec)

mysql> show tables;
+------------------------+
| Tables_in_normalize_db |
+------------------------+
| results_sheet          |
+------------------------+
1 row in set (0.00 sec)
```

### 3-2. 第1正規形

1. ID
2. Student Code(int)
3. Student Name(string)
4. Subject Code(英語+int)
5. Subject Name(string)
6. Academic Year(int)
7. Results (string)

(id int, name varchar(10));

insert into user values (1, 'Yamada', 'Tokyo');
