package submit

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"main.go/check"
	"main.go/database"
	"os"
	"strconv"
	"strings"
	"time"
)

func SubmitDecryPython(c *gin.Context) {
	var code DecryptCodeSubmit
	var submit database.SubmitRecord
	var userChallenge database.UserChallenge

	c.BindJSON(&code)
	token := c.Request.Header.Get("Authorization")
	cid := c.Param("cid")
	intcid, err := strconv.Atoi(cid)
	if err != nil {
		c.JSON(400, gin.H{
			"code": 400,
			"err":  "非法的cid",
		})
	}

	//判断token是否正确
	if !IsTokenValid(c) {
		c.JSON(200, gin.H{
			"code": InvalidTokenError,
			"msg":  "无效的令牌",
		})
		return
	}
	uid := GetIDByToken(token)

	//判断是否可以使用解密
	if Candecrypt(intcid, uid) != true {
		c.JSON(200, gin.H{
			"code": 400,
			"msg":  "你没有权限使用解密",
		})
		return
	}

	code.DecryptCode = strings.Replace(code.DecryptCode, "\\n", "\n", -1)
	code.DecryptCode = strings.Replace(code.DecryptCode, "\\t", "\t", -1)
	code.DecryptCode = strings.Replace(code.DecryptCode, "\\r", "\r", -1)

	decryfilename := "decry.py"
	tokenpath := "/home/ctf/codefile/" + token + "/"
	_, err = os.Stat(tokenpath)
	if err != nil {
		err = os.Mkdir(tokenpath, 0777)
		if err != nil {
			c.JSON(200, gin.H{
				"code": WriteFileError,
				"msg":  "创建文件夹失败",
			})
			return
		}
	}
	decryfilepath := tokenpath + decryfilename
	//拼接代码
	finalcode := DecryptCodeSplicing(code.DecryptCode)
	err = os.WriteFile(decryfilepath, []byte(finalcode), 0666)
	if err != nil {
		c.JSON(200, gin.H{
			"code": WriteFileError,
			"msg":  "写入文件失败",
		})
		return
	}
	//开始创建run.sh
	secretdata := GetSecretData(intcid)
	runbash := CreateBash2(secretdata)
	runbashpath := tokenpath + "run.sh"
	err = ioutil.WriteFile(runbashpath, []byte(runbash), 0666)
	if err != nil {
		c.JSON(200, gin.H{
			"code": WriteFileError,
			"msg":  "写入文件失败",
		})
		return
	}

	submit.UserID = uid
	submit.SubmitTime = time.Now()
	submit.Language = code.Language

	codetype, result1, times, memroy, err := RunDecry(tokenpath, DockerImage)
	if codetype != Success {
		submit.DecryptCode = code.DecryptCode
		submit.Status = codetype
		submit.Memory = 0
		submit.RunTime = 0
		submit.ChallengeID = intcid
		DB.Create(&submit)

		c.JSON(200, gin.H{
			"code": codetype,
			"msg":  result1,
		})
		return
	}

	times = times / time.Millisecond
	codetype, err = check.Dechecker(intcid, result1)
	if err != nil {
		submit.DecryptCode = code.DecryptCode
		submit.Status = codetype
		submit.Memory = 0
		submit.RunTime = 0
		submit.ChallengeID = intcid

		DB.Create(&submit)

		c.JSON(200, gin.H{
			"code": codetype,
			"msg":  err.Error(),
		})
		return
	}

	if codetype == Success {
		submit.DecryptCode = code.DecryptCode
		submit.Status = Success
		submit.Memory = memroy
		submit.RunTime = times
		submit.ChallengeID = intcid
		DB.Create(&submit)

		DB.Where("user_id = ? AND challenge_id = ?", uid, cid).First(&userChallenge)
		userChallenge.IsSolved = true
		DB.Save(&userChallenge)

		c.JSON(200, gin.H{
			"code":   Success,
			"msg":    "解密成功",
			"times":  times,
			"memroy": memroy,
		})
		return
	}

}

func Candecrypt(cid int, uid int) bool {
	DB, _ := database.GetDB()
	var userChallenge database.UserChallenge
	DB.Where("user_id = ? AND challenge_id = ?", uid, cid).First(&userChallenge)
	if userChallenge.IsEnCrypt == true {
		return true
	}
	return false

}

func CreateBash2(secret string) string {
	//将secret以,分割
	secretlist := strings.Split(secret, ",")
	bash := "#!/bin/bash\nset -e\n"
	for i, _ := range secretlist {
		//python decry.py png
		bash += fmt.Sprintf("python decry.py %s\n", "png/"+strconv.Itoa(i+1)+"_encry_attacked.png")
	}
	return bash
}

func DecryptCodeSplicing(code string) string {
	codeTop := `import sys
from PIL import Image
import numpy as np
import builtins


`

	codeBottom :=
		`

def print(*args, **kwargs):
    pass

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv)!=2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    secret = s.Decrypt(img)
    print = builtins.print
    print(secret)
    

`
	splicedCode := fmt.Sprintf("%s\n%s\n%s", codeTop, code, codeBottom)
	return splicedCode

}
