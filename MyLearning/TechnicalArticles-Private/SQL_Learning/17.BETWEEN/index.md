# 17. BETWEEN
**指定された範囲内の値を選択します。**
値は、**数値、テキスト、または日付**にすることができます。

- 構文
```sql: BETWEEN
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

## 17-1. DemoDatabase
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
`SELECT * FROM Products;`に変更して実行してください。

## 17-2. BETWEENの実行
- Priceが10~20の全ての製品を選択する

```sql: BETWEEN
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```
![](2022-08-28-22-11-23.png)

## 17-3. NOT BETWEENの実行
- `17-2`の範囲外の製品の選択

```sql: NOT BETWEEN
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```
![](2022-08-28-22-13-10.png)

## 17-4. INを使用したBETWEENの実行
1. Priceが10~20の全ての製品を選択する
2. ただし、CategoryIDが`1, 2, 3`の製品を表示しない

```sql: BETWEEN & IN
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1, 2, 3);
```
![](2022-08-28-22-16-57.png)

- 2を条件に入れなかった場合
![](2022-08-28-22-16-12.png)

## 17-5. BETWEEN (テキスト値)
- `Carnarvon Tigers`と`Mozzarella di Giovanni`の間のProductNameを持つ全ての製品を選択する

```sql: BETWEEN(text)
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
```
![](2022-08-28-22-18-43.png)
:::message
今回指定しているのは`人名`です。
1と2の間の、というのはアルファベット順で1〜2の間の人のデータを取ってきています。(1と2も含む)
:::

```sql: BETWEEN(text)
SELECT * FROM Products
WHERE ProductName BETWEEN "Carnarvon Tigers" AND "Chef Anton's Cajun Seasoning"
ORDER BY ProductName;
```
![](2022-08-28-22-23-44.png)
こっちの方が分かりやすいですね

## 17-6. NOT BETWEEN (テキスト値)
- `17-5`ではない結果を表示します。

```sql: NOT BETWEEN
SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
```
![](2022-08-28-22-26-52.png)
:::message
注目すべきはProductID60と30の間が抜けていることです。
:::

## 17-7. DemoDatabase
`SELECT * FROM Orders;`を実行してください。
Ordersテーブルを使用します。

## 17-8. BETWEEN (日付)
- OrderDataが'01-July-1996' から '31-July-1996' の間のすべての注文を選択します。

```sql: BETWEEN(Date)
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;
```
または:
```sql: BETWEEN(Date)
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```
![](2022-08-28-22-33-13.png)
同じ結果が得られます。

