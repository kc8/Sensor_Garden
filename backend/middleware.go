package main

import (
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

const (
	AUTH_HEADER string = "AUTH-HEADER"
)

func AuthWrapper() gin.HandlerFunc {
	return authIntercept
}

//TODO add in auth service provider connection
func authIntercept(c *gin.Context) {
	authHeader := c.GetHeader(AUTH_HEADER)
	if authHeader == "" {
		log.Println("Invalid auth recieved aborting connection")
		c.Status(http.StatusUnauthorized)
		c.Abort()
	}
}
