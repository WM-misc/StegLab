package check

import (
	"ctf/database"
	"github.com/gin-gonic/gin"
)

//检查是否可以使用解密
func CanUseDecode(c *gin.Context) {
	DB, _ := database.GetDB()
	var userChallenge database.UserChallenge
	token := c.Request.Header.Get("Authorization")
	cid := c.Param("cid")
	uid := GetIDByToken(token)
	DB.Where("user_id = ? AND challenge_id = ?", uid, cid).First(&userChallenge)
	if userChallenge.IsEnCrypt == true {
		c.JSON(200, gin.H{
			"code":    0,
			"encrypt": true,
		})
	} else {
		c.JSON(200, gin.H{
			"code":    0,
			"encrypt": false,
		})
	}
}

func GetIDByToken(token string) int {
	var user database.User
	DB, _ := database.GetDB()
	DB.Where("token = ?", token).First(&user)
	return user.ID
}
