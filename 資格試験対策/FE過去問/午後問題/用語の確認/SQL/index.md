## UNION
UNIONは、表を統合して1つの結果を求める
※重複は削除される

例: 表R, Sを統合する
```c
select * from R
UNION
select * from S
```

## ビューの作成
CREATE VIEW文を使用する

`CREATE VIEW ビュー名 AS 定義;`

定義の部分には、実際にビューとして表示する内容を取得する「SELECT文」を記述する

> - ビューはテーブルと同じようなもの
> - ただし、テーブルには実際のデータが保存されているのに対し、
