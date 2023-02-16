package service

import (
	"context"
	"gqlgen_tutorial/app/entity"
)

type Service interface {
	QueryService
}

type QueryService interface {
	GetCompany(ctx context.Context) *entity.Company
}
