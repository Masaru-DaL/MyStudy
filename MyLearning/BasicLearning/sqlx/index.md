# sqlx

## Databaseとの接続の違い

- database/sql

```go:
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

- sqlx

```go:
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
