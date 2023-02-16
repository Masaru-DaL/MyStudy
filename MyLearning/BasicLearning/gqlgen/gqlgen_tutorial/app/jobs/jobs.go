package jobs

import (
	"context"
	"gqlgen_tutorial/app/entity"
	"log"

	"github.com/jmoiron/sqlx"
)

func GetCompany(ctx context.Context, db *sqlx.DB) (*entity.Company, error) {
	sqlStatement := "SELECT * FROM users WHERE id = ?"

	company := &entity.Company{}
	err := db.GetContext(ctx, company, sqlStatement)
	if err != nil {
		log.Printf("Failed to GetContext for a single retrieval operation in the users: %v", err)
		return nil, err
	}

	return company, nil
}
