# 15. Wildcards
**文字列内の1つ以上の文字を置き換えるために使用される**
- 演算子にはワイルドカード文字が使用される
- 演算子は、列で指定されたパターンを検索するために、`WHERE`, `LIKE`などの句で使用される

![](2022-08-27-12-49-02.png)

![](2022-08-27-12-49-16.png)


## 15-1. DemoDatabase
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

## 15-2-1. % ワイルドカードの使用
- Cityが`ber`で始まる全ての顧客を選択する

```sql: %
SELECT * FROM Customers
WHERE City LIKE 'ber%';
```
![](2022-08-27-12-51-30.png)
:::message
~で始まる -> ~% のように%の前に文字列を指定する。
~で終わる -> %~ のように%の後ろに文字列を指定する
:::

## 15-2-2. % ワイルドカードの使用
- Cityに`es`を含む全ての顧客を選択する

```sql: %
SELECT * FROM Customers
WHERE City LIKE '%es%';
```
![](2022-08-27-12-54-36.png)
:::message
~を含む -> %~% のように任意の文字列を%で囲む
:::

