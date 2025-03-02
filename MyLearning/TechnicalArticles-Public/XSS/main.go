// code:web3-4 main.go
package main

import (
	"log"
	"net/http"
)

func main() {
	port := "8080"

	http.Handle("/", http.FileServer(http.Dir("root/"))) // ①
	log.Printf("Server listening on http://localhost:%s/", port)
	log.Print(http.ListenAndServe(":"+port, nil))
}
