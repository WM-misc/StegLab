package main

import "ctf/router"

func main() {
	rout := router.Router()
	rout.Run(":8080")
}
