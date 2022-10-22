package main

import (
	"log"
	"net/http"
)

func main() {
	/* ディレクトリを指定する */
	fs := http.FileServer(http.Dir("static"))
	/* /にアクセスがきたら指定したディレクトリのコンテンツを表示 */
	http.Handle("/", fs)

	log.Println("Listening...")
	http.ListenAndServe(":3000", nil)
}
