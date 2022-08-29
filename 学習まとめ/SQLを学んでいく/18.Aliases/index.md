# 18. Aliases
**テーブル、またはテーブルの内の列に一時的な名前を付けるために使用されます。**
別名は、**列名を読みやすくするため**によく使用されます。
Aliasesは、そのクエリの間だけ存在します。
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


## 18-1.
