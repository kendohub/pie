package main

import (
	"fmt"
	"log"
	"net/http"
)

func handlerA(w http.ResponseWriter, r *http.Request) {
	for distance := 50; distance <= 150; distance++ {
		fmt.Fprintf(w, "%s: %d\n", r.URL.Path[1:], distance)
	}
}

func handlerB(w http.ResponseWriter, r *http.Request) {
	for distance := 0.0; distance <= 150.0; distance += 1.5 {
		fmt.Fprintf(w, "%s: %.1f\n", r.URL.Path[1:], distance)
	}
}

func main() {
	http.HandleFunc("/a_san", handlerA)
	http.HandleFunc("/b_san", handlerB)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
