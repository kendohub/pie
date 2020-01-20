package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	for i := 0; i <= 150; i++ {
		fmt.Fprintf(w, "%d\n", r.URL.Path[1:])
	}
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
