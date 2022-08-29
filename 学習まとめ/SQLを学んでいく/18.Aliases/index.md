# 18. Aliases
**テーブル、またはテーブルの内の列に一時的な名前を付けるために使用されます。**
別名は、**列名を読みやすくするため**によく使用されます。
Aliasesーー、そのクエリの間だけ存在します。
Aliasesは`AS`というキーワードで作成されます。

- 構文
```sql: Aliases
SELECT column_name AS alias_name
FROM table_name;
```

- AliasesTableの構文
```sql: AliasesTable
SELECT column_name(s)
FROM table_name AS alias_name;
```

## 18-1. DemoDatabase
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

CustomersTable & OrdersTableの2つを使用

## 18-2-1. Aliases (列)
- CustomerIDをIDに、CustomerNameをCustomerに変更して、表示する

```sql: Aliases
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
```

## 18-2-2. Aliases (列)
- CustomerNameをCustomerに、ContactNameをContact Personに変更して、表示する

```sql: Aliases
SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;
```
:::message
エイリアス名にスペースを含む場合は二重引用符、または角括弧が必要です。
:::


