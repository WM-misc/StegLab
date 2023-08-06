package submit

import (
	"ctf/database"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"net/http"
)

func GetMd5ByToken(token string) string {
	var user database.User
	err := DB.Where("token = ?", token).First(&user).Error
	if err != nil {
		panic(err)
	} else {
		return user.NameMd5
	}
}

func GetFlag(c *gin.Context) {
	var userChallenge database.UserChallenge
	token := c.Request.Header.Get("Authorization")
	teamname := c.Request.Header.Get("Teamname")
	cid := c.Param("cid")
	uid := GetIDByToken(token)
	DB.Where("user_id = ? AND challenge_id = ?", uid, cid).First(&userChallenge)

	if userChallenge.IsSolved == true {
		if cid != "2" {
			c.JSON(200, gin.H{
				"code": Success,
				"msg":  "获取flag成功",
				"flag": "flag{flag}",
			})
			return
		}
		flagurl := UserGetFlagUrl + token + "&teamname=" + teamname
		resp, err := http.Get(flagurl)
		if err != nil {
			c.JSON(200, gin.H{
				"code": SomeError,
				"msg":  "获取flag失败",
			})
		}
		defer resp.Body.Close()
		d1, _ := ioutil.ReadAll(resp.Body)
		data := JsonNew.Get(d1)
		c.JSON(200, gin.H{
			"code": Success,
			"msg":  "获取flag成功",
			"flag": data.Get("data").ToString(),
		})
	} else {
		c.JSON(200, gin.H{
			"code": SomeError,
			"msg":  "未解决",
		})
	}

}
