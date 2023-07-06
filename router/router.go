package router

import (
	"errors"
	"github.com/gin-gonic/gin"
	"main.go/challenge"
	"main.go/check"
	"main.go/database"
	"main.go/submit"
	"net/http"
)

func Router() *gin.Engine {
	r := gin.Default()
	r.Use(Cors())
	auth := r.Group("/api/v1")
	auth.POST("/set-token", func(c *gin.Context) {
		DB, _ := database.GetDB()
		var request submit.TokenRequest
		var User database.User
		if err := c.BindJSON(&request); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "无效的请求参数"})
			return
		}

		token := request.Token
		if token != "" {
			c.SetCookie("token", token, 3600, "/", "172.21.26.127", false, true)
			DB.Where("token = ?", request.Token).First(&User)
			if User.Token == "" {
				DB.Create(&database.User{
					Token: token,
				})
			}
			c.JSON(http.StatusOK, gin.H{"code": submit.TokenTrue, "message": "Token设置成功。", "token": token})
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Token不能为空。"})
		}

	})

	auth.Use(AuthMiddleWare())
	{
		auth.POST("/submitencry/:cid", submit.SubmitEncryPython)
		auth.POST("/submitdecry/:cid", submit.SubmitDecryPython)
		auth.GET("/gethistory/:cid", submit.GetHistory)
		auth.GET("/check/:cid", check.CanUseDecode)
		auth.POST("/newchallenge", challenge.CreateNewChallenge)
		auth.GET("/getchallenge/:cid", challenge.GetChallengeInfo)
		auth.GET("/getchallengelist", challenge.GetChallengeList)
		auth.GET("/isSolve/:cid", challenge.IsSolve)
	}
	return r
}

//允许跨域
func Cors() gin.HandlerFunc {
	return func(c *gin.Context) {
		method := c.Request.Method
		origin := c.Request.Header.Get("Origin")
		if origin != "" {
			c.Header("Access-Control-Allow-Origin", "*") // 可将将 * 替换为指定的域名
			c.Header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE, UPDATE")
			c.Header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization")
			c.Header("Access-Control-Expose-Headers", "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Cache-Control, Content-Language, Content-Type")
			c.Header("Access-Control-Allow-Credentials", "true")
		}
		if method == "OPTIONS" {
			c.AbortWithStatus(http.StatusNoContent)
		}
		c.Next()
	}
}

//中间件
func AuthMiddleWare() gin.HandlerFunc {
	return func(c *gin.Context) {
		//token, err := c.Cookie("token")
		//设置为Authorization
		token := c.Request.Header.Get("Authorization")
		//fmt.Println(token)

		if token == "" {
			err := errors.New("未提供有效令牌")
			c.JSON(http.StatusUnauthorized, gin.H{"error": err.Error()})
			c.Abort()
			return
		}
		c.Next()
	}
}
