package check

import (
	"ctf/database"
	"errors"
	"strconv"
	"strings"
)

func Enchecker(cid int, stdout string) (int, error) {
	//如果stdout包含Error，返回错误
	if strings.Contains(stdout, "Error") {
		return 4, nil
	}
	//后续再修改
	DB, _ := database.GetDB()
	var challenge database.Challenge
	DB.Where("id = ?", cid).First(&challenge)
	//分割DB中的secretData
	secretData := strings.Split(challenge.Data, ",")
	//分割stdout
	stdoutlist := strings.Split(stdout, "\n")
	//删掉空行
	for i := 0; i < len(stdoutlist); i++ {
		if stdoutlist[i] == "" {
			stdoutlist = append(stdoutlist[:i], stdoutlist[i+1:]...)
		}
	}

	//统计Nop的个数
	nopnums := 0
	for i, _ := range stdoutlist {
		if stdoutlist[i] == "NOP" {
			nopnums++
		}
	}
	msg := "[" + strconv.Itoa(nopnums) + "/" + strconv.Itoa(len(secretData)) + "]"
	if nopnums > 0 {
		return 4, errors.New(msg)
	}

	return 0, nil
}

func Dechecker(cid int, stdout string) (int, error) {
	if strings.Contains(stdout, "Error") {
		return 4, errors.New(stdout)
	}
	DB, _ := database.GetDB()
	var challenge database.Challenge
	DB.Where("id = ?", cid).First(&challenge)
	secretData := strings.Split(challenge.Data, ",")
	stdoutlist := strings.Split(stdout, "\n")
	for i := 0; i < len(stdoutlist); i++ {
		if stdoutlist[i] == "" {
			stdoutlist = append(stdoutlist[:i], stdoutlist[i+1:]...)
		}
	}
	//逐一对比secretData和stdoutlist，最后返回【8/8】这种的进度
	successnums := 0
	msg := "[" + strconv.Itoa(successnums) + "/" + strconv.Itoa(len(secretData)) + "]"
	for i, _ := range secretData {
		//如果stdoutlist in secretData中
		if strings.Contains(stdoutlist[i], secretData[i]) {
			successnums++
			msg = "[" + strconv.Itoa(successnums) + "/" + strconv.Itoa(len(secretData)) + "]"
		} else {
			return 4, errors.New(msg)
		}
	}
	return 0, nil

}
