package main

import (
	"gqlgen_tutorial/app/graph"
	"gqlgen_tutorial/app/graph/generated"
	"gqlgen_tutorial/app/infra/mysql"
	"log"

	"github.com/99designs/gqlgen/graphql/handler"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

const defaultPort = "8082"

func main() {
	// DBに接続する
	db, err := mysql.NewSQLClient()
	if err != nil {
		log.Fatalf("failed to connect to database: %v", err)
	}
	defer db.Close()

	// Echoのインスタンスを作成する
	e := echo.New()

	// GraphQLのエンドポイントを定義する
	e.POST("/query", func(c echo.Context) error {
		h := handler.GraphQL(generated.NewExecutableSchema(generated.Config{Resolvers: &graph.Resolver{DB: db}}))
		h.ServeHTTP(c.Response(), c.Request())
		return nil
	})

	// Echoの設定
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// サーバーを起動する
	if err := e.Start(":8082"); err != nil {
		log.Fatalf("failed to start server: %v", err)
	}
}
