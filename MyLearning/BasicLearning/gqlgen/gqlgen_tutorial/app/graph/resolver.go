package graph

import "gqlgen_tutorial/app/graph/usecase/service"

// This file will not be regenerated automatically.
//
// It serves as dependency injection for your app, add any dependencies you require here.

type Resolver struct {
	S service.Service
}

func NewResolver(s service.Service) *Resolver {
	return &Resolver{
		S: s,
	}
}
