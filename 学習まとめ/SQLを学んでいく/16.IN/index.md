# 16. IN
**WHERE句で複数の値を指定できる**

- 構文
```sql: IN
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```
または:
```sql: IN
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```

## 16-1. DemoDatabase

