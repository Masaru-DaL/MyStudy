# 10. DELETE
**テーブル内の既存レコードを削除するために使用される**

- DELETE 構文
```sql: DELETE
DELETE FROM table_name WHERE condition;
```

## 10-1. DemoDatabase
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

## 10-2. DELETEの実行
- Customersテーブルから'Alfreds Futterkiste'を削除する

1. `Restore Database`でデーターベースを初期化します。
![](2022-08-22-20-09-36.png)

2. DELETE文を実行します。
![](2022-08-22-20-10-34.png)

1であったCusmerID1のデータが消えています。
そして、`Number of Recorsds`が91 -> 90に減っている事から、データの削除が確認出来ました。
