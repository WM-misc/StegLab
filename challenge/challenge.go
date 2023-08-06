package challenge

import (
	"ctf/database"
	"ctf/submit"
	"github.com/gin-gonic/gin"
)

var DB, _ = database.GetDB()

func CreateNewChallenge(c *gin.Context) {
	var challenge database.Challenge
	c.BindJSON(&challenge)
	DB.Create(&challenge)
	c.JSON(200, gin.H{
		"code": 0,
		"msg":  "创建成功",
	})
}

func GetChallengeList(c *gin.Context) {
	var challenge []database.Challenge
	DB.Find(&challenge)
	c.JSON(200, gin.H{
		"code": 0,
		"msg":  "获取成功",
		"data": challenge,
	})
}

func GetChallengeInfo(c *gin.Context) {
	var challenge database.Challenge
	cid := c.Param("cid")
	DB.Where("id = ?", cid).First(&challenge)
	c.JSON(200, gin.H{
		"code": 0,
		"msg":  "获取成功",
		"data": challenge,
	})
}

func IsSolve(c *gin.Context) {
	var userChallenge database.UserChallenge
	token := c.Request.Header.Get("Authorization")
	cid := c.Param("cid")
	uid := submit.GetIDByToken(token)
	DB.Where("user_id = ? AND challenge_id = ?", uid, cid).First(&userChallenge)
	if userChallenge.IsSolved == true {
		c.JSON(200, gin.H{
			"code": submit.IsSolved,
			"msg":  "已经解决",
		})
	} else {
		c.JSON(200, gin.H{
			"code": submit.NoneSolved,
			"msg":  "未解决",
		})
	}
}
