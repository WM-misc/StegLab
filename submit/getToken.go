package submit

import (
	"ctf/database"
	"encoding/base64"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
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
	var flagurl string
	dteamname, _ := base64.StdEncoding.DecodeString(teamname)
	teamname = string(dteamname)
	if userChallenge.IsSolved == true {
		//只有第二题第三题有flag
		if cid == "2" {
			flagurl = UserGetFlagUrl + token + "&teamname=" + teamname
		}
		if cid == "3" {
			flagurl = UserGetFlagUrl2 + token + "&teamname=" + teamname
		}
		if cid != "2" && cid != "3" {
			c.JSON(200, gin.H{
				"code": Success,
				"msg":  "获取flag成功",
				"flag": "flag{test_flag}",
			})
			return
		}
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
