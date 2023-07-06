package submit

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"main.go/check"
	"main.go/database"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

var DB, _ = database.GetDB()

func SubmitEncryPython(c *gin.Context) {

	var code EncryptCodeSubmit
	var submit database.SubmitRecord
	var userChallenge database.UserChallenge

	c.BindJSON(&code)
	//获取token
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

	code.EncryptCode = strings.Replace(code.EncryptCode, "\\n", "\n", -1)
	code.EncryptCode = strings.Replace(code.EncryptCode, "\\t", "\t", -1)
	code.EncryptCode = strings.Replace(code.EncryptCode, "\\r", "\r", -1)
	encryfilename := "encry.py"
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
	encryfilepath := tokenpath + encryfilename
	//拼接代码
	finalcode := CodeSplicing(code.EncryptCode)
	err = ioutil.WriteFile(encryfilepath, []byte(finalcode), 0666)
	if err != nil {
		c.JSON(200, gin.H{
			"code": WriteFileError,
			"msg":  "写入文件失败",
		})
		return
	}
	//开始创建run.sh
	secretdata := GetSecretData(intcid)
	runbash := CreateBASHRun(secretdata)
	runbashpath := tokenpath + "run.sh"
	err = ioutil.WriteFile(runbashpath, []byte(runbash), 0666)
	if err != nil {
		c.JSON(200, gin.H{
			"code": WriteFileError,
			"msg":  "写入文件失败",
		})
		return
	}
	//复制PNGPATH到选手文件夹
	userPNGPATH := tokenpath + "png/"
	exec.Command("rm", "-rf", userPNGPATH).Run()
	//复制PNGPATH到选手文件夹,执行cp命令
	exec.Command("cp", "-r", PNGPATH, userPNGPATH).Run()

	//复制attack.py到选手文件夹
	attackpath := "/home/ctf/codefile/attack.py"
	userattackpath := tokenpath + "attack.py"
	exec.Command("cp", attackpath, userattackpath).Run()

	//psnr.py
	psnrpath := "/home/ctf/codefile/psnr.py"
	userpsnrpath := tokenpath + "psnr.py"
	exec.Command("cp", psnrpath, userpsnrpath).Run()

	submit.UserID = GetIDByToken(token)

	submit.SubmitTime = time.Now()
	submit.Language = code.Language

	codetype, result1, times, memroy, err := RunEncry(tokenpath, DockerImage)
	if codetype != Success {

		//提交失败，写入数据库
		submit.EncryptCode = code.EncryptCode
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
	codetype, err = check.Enchecker(intcid, result1)
	if err != nil {

		submit.EncryptCode = code.EncryptCode
		submit.Status = codetype
		submit.Memory = memroy
		submit.RunTime = times
		submit.ChallengeID = intcid

		DB.Create(&submit)

		c.JSON(200, gin.H{
			"code": codetype,
			"msg":  err.Error(),
		})
		return
	}

	if codetype == Success {
		//提交成功，写入数据库
		submit.EncryptCode = code.EncryptCode
		submit.Status = Success
		submit.Memory = memroy
		submit.RunTime = times
		submit.ChallengeID = intcid

		DB.Create(&submit)
		//更新用户题目状态
		DB.Where("user_id = ? AND challenge_id = ?", submit.UserID, submit.ChallengeID).First(&userChallenge)
		userChallenge.IsEnCrypt = true
		DB.Save(&userChallenge)
		c.JSON(200, gin.H{
			"code":   Success,
			"msg":    "加密成功",
			"times":  times,
			"memroy": memroy,
		})
		return
	}
}

func GetIDByToken(token string) int {
	var user database.User
	DB.Where("token = ?", token).First(&user)
	return user.ID
}

func GetSecretData(id int) string {
	var challenge database.Challenge
	DB.Where("id = ?", id).First(&challenge)
	return challenge.Data
}

func CreateBASHRun(secret string) string {
	//将secret以,分割
	secretlist := strings.Split(secret, ",")
	bash := "#!/bin/bash\nset -e\n"
	for i, v := range secretlist {
		//python encry.py img key
		bash += fmt.Sprintf("python encry.py %s %s\n", "png/"+strconv.Itoa(i+1)+".png", v)
	}
	for i, _ := range secretlist {
		bash += fmt.Sprintf("python psnr.py %s %s\n", "png/"+strconv.Itoa(i+1)+".png", "png/"+strconv.Itoa(i+1)+"_encry.png")

	}
	for i, _ := range secretlist {
		bash += fmt.Sprintf("python attack.py %s\n", "png/"+strconv.Itoa(i+1)+"_encry.png")
	}

	//bash += "rm -rf run.sh\n"
	return bash
}

//拼接代码
func CodeSplicing(code string) string {
	codeTop :=
		`import sys
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
    if len(sys.argv)!=3:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    key = sys.argv[2]
    encryimg = s.Encrypt(img,key)
    encryimg.save(img[:-4]+"_encry.png")

`

	splicedCode := fmt.Sprintf("%s\n%s\n%s", codeTop, code, codeBottom)
	return splicedCode
}

func WriteAttack() {}
