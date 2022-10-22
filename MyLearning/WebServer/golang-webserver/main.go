package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriterm r *http.Request) {
	fmt.Fprintf(w, "Hello, World")
}

func main() {
	http.HandlerFunc("/", handler)
	http.ListenAndServer(":8000", nil)
}
