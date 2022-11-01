# 14. LIKE
**列で指定されたパターンを検索するために使用されます**

- LIKEと組み合わせてよく使用される2つのワイルドカード
  - パーセント記号(%)
    - 0, 1, または複数の文字を表す
  - アンダースコア記号(_)
    - 1つの単一文字を表す

- 構文
```sql: LIKE
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```
:::message
AND or OR演算子を使用して、任意の数の条件を組み合わせることもできる。
:::


## 14-1. DemoDatabase
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

## 14-2. LIKEの実行
#### 14-2-1. LIKE 'a%'
- `a`で始まるCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.1
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';
```
![](2022-08-26-07-41-33.png)

#### 14-2-2. LIKE '%a'
- `a`で終わるCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.2
SELECT * FROM Customers
WHERE CustomerName LIKE '%a';
```
![](2022-08-26-07-43-32.png)

#### 14-2-3. LIKE '%or%'
- 任意の位置に`or`があるCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.3
SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';
```
![](2022-08-26-16-22-24.png)
Antonio M**or**eno Taqueria
Around the H**or**n などがヒットします。

#### 14-2-4. LIKE '_r%'
- 2番目の位置に`r`を持つCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.4
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';
```
![](2022-08-27-10-05-29.png)

#### 14-2-5. LIKE 'a__%'
- `a`で始まり、長さが3文字以上のCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.5
SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';
```
![](2022-08-27-10-07-44.png)

#### 14-2-6. LIKE
- `a`で始まり、長さが3文字以上のCustomerNameを持つ全ての顧客を選択する

```sql: LIKE.6
SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';
```
![](2022-08-27-12-03-54.png)

#### 14-2-7. LIKE 'a%o'
- `a`で始まり、`o`で終わるContactNameを持つ全ての顧客を選択する

```sql: LIKE.7
SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';
```
![](2022-08-27-12-06-44.png)

#### 14-2-8. NOT LIKE 'a%'
- `a`で始まらないCustomerNameを持つ全ての顧客を選択する

```sql: NOT LIKE
SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';
```
![](2022-08-27-12-09-24.png)
