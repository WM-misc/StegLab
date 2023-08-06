package submit

import jsoniter "github.com/json-iterator/go"

var JsonNew = jsoniter.ConfigCompatibleWithStandardLibrary
var DockerImage = "ctf:v1"
var UUID = "fa1c7bea-b769-4520-87a1-5e0f0112b98c"
var UserExistUrl = "https://flagserver.wm-team.cn/exist?uuid=" + UUID + "&teamtoken="
var UserGetFlagUrl = "https://flagserver.wm-team.cn/getFlag?uuid=" + UUID + "&teamtoken="

type TokenRequest struct {
	Token    string `json:"token"`
	TeamName string `json:"teamname"`
}

type EncryptCodeSubmit struct {
	EncryptCode string `json:"encrypt_code"`
	Language    string `json:"language"`
}
type DecryptCodeSubmit struct {
	DecryptCode string `json:"decrypt_code"`
	Language    string `json:"language"`
}

const PNGPATH = "/home/ctf/codefile/png/"

//定义返回code状态码
const (
	Success      = 0 //成功
	SomeError    = 1 //部分成功
	CodeError    = 2 //代码错误
	CompileError = 3 //编译错误
	RunningError = 4 //运行错误
	TimeoutError = 5 //超时
	MemoryError  = 6 //超出内存限制
	DockerError  = 7 //Docker错误

	WriteFileError    = 8 //写入文件失败
	InvalidTokenError = 9 //Token无效

	TokenTrue = 10 //Token正确

	IsSolved   = 11 //已经解决
	NoneSolved = 12 //未解决

)
