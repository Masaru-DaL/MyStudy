# 13. COUNT() / AVG() / SUM()
COUNT()関数は、**指定された条件に一致する行数を返します**。
AVG()関数は、**数値列の平均値を返します**。
SUM()関数は、**数値列の合計を返します**。

- COUNT()構文
```sql: COUNT
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

- AVG()構文
```sql: AVG
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

- SUM()構文
```sql: SUM
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```
