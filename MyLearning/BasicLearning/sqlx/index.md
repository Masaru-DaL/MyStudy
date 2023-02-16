# sqlx

## 2. Databaseとの接続の違い

### 2-1. database/sql

```go: db.go
package db

import (
	"log"
	"src/internal/config"

	"github.com/jmoiron/sqlx"
	_ "github.com/mattn/go-sqlite3"
)

func ConnectDatabase() *sqlx.DB {
	config.LoadConfigForYaml()

	db, err := sqlx.Open(config.Config.DB.SQLDriver, config.Config.DB.DBPath)
	if err != nil {
		log.Fatal(err)
	}

	// エラーは出なかったが、何らかの理由でデータベース接続ができなかった場合
	if db == nil {
		log.Fatal(err)
	}

	/* 接続が可能であることを確認する */
	err = db.Ping()
	if err != nil {
		defer db.Close()
	}

	return db
}
```

### 2-2. sqlx

```go: db.go
package db

import (
	"log"
	"src/internal/config"

	"github.com/jmoiron/sqlx"
	_ "github.com/mattn/go-sqlite3"
)

func ConnectDatabase() *sqlx.DB {
	config.LoadConfigForYaml()

	db, err := sqlx.Open(config.Config.DB.SQLDriver, config.Config.DB.DBPath)
	if err != nil {
		log.Fatal(err)
	}

	// エラーは出なかったが、何らかの理由でデータベース接続ができなかった場合
	if db == nil {
		log.Fatal(err)
	}

	/* 接続が可能であることを確認する */
	err = db.Ping()
	if err != nil {
		defer db.Close()
	}

	return db
}
```

## 3. 関数の違い

### 3-1. database/sql

```go: users.go
package users

import (
	"database/sql"
	"log"
	"src/internal/entity"
)

/*
ユーザ情報の1件取得
指定した名前のユーザの情報を取得する
*/
func UserReqUsername(db *sql.DB, username string) (entity.User, error) {
	sqlStatement := "SELECT * FROM users WHERE name = ?"

	stmt, err := db.Prepare(sqlStatement)
	if err != nil {
		log.Printf("Failed to Prepare for a single retrieval operation in the users: %v", err)
		return entity.User{}, err
	}
	defer stmt.Close()

	user := entity.User{}
	err = stmt.QueryRow(username).Scan(
		&user.ID,
		&user.Name,
		&user.Password,
		&user.Email,
		&user.IsAdmin,
		&user.CreatedAt,
		&user.UpdatedAt)
	if err != nil {
		log.Printf("Failed to QueryRow for a single retrieval operation in the users: %v", err)
		return entity.User{}, err
	}

	return user, err
}
```

### 3-2. sqlx

```go: users.go
package users

import (
	"github.com/jmoiron/sqlx"
	"log"
	"github.com/example/entity"
)

func GetUserByUsername(db *sqlx.DB, username string) (entity.User, error) {
	sqlStatement := "SELECT * FROM users WHERE name = ?"

	user := entity.User{}
	err := db.Get(&user, sqlStatement, username)
	if err != nil {
		log.Printf("Failed to Get for a single retrieval operation in the users: %v", err)
		return entity.User{}, err
	}

	return user, nil
}
```
