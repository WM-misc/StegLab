package main

import "main.go/router"

func main() {
	rout := router.Router()
	rout.Run(":8080")
}
