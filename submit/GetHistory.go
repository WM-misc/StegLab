package submit

import (
	"ctf/database"
	"github.com/gin-gonic/gin"
	"strconv"
)

func GetHistory(c *gin.Context) {
	DB, _ := database.GetDB()
	var submit []database.SubmitRecord
	token := c.Request.Header.Get("Authorization")
	teamname := c.Request.Header.Get("Teamname")
	cid := c.Param("cid")
	//判断token是否正确
	if !IsTokenValid(token, teamname) {
		c.JSON(200, gin.H{
			"code": InvalidTokenError,
			"msg":  "无效的令牌",
		})
		return
	}

	uid := GetIDByToken(token)
	CreateUserChallenge(uid, cid)
	DB.Where("user_id = ? AND challenge_id = ?", uid, cid).Find(&submit)
	c.JSON(200, gin.H{
		"code": 0,
		"msg":  "获取成功",
		"data": submit,
	})

}

func CreateUserChallenge(uid int, cid string) {
	var userChallenge database.UserChallenge
	DB, _ := database.GetDB()
	var count int64
	intcid, _ := strconv.Atoi(cid)
	DB.Model(&database.UserChallenge{}).Where("user_id = ? AND challenge_id = ?", uid, cid).
		Count(&count)

	if count == 0 {
		userChallenge.UserID = uid
		userChallenge.ChallengeID = intcid
		userChallenge.IsEnCrypt = false
		userChallenge.IsSolved = false
		DB.Create(&userChallenge)
	}

}
