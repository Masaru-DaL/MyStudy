package mysql

import "github.com/jmoiron/sqlx"

func NewSQLClient() (*sqlx.DB, error) {
	db, err := sqlx.Open("mysql", "app/infra/db/database.db")
	if err != nil {
		return nil, err
	}

	return db, nil
}
