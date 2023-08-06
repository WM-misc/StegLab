package database

import "time"

type User struct {
	ID       int    `gorm:"primaryKey"`
	Token    string `gorm:"column:token" json:"token"`
	TeamName string `gorm:"column:teamname" json:"teamname"`
	NameMd5  string `gorm:"column:name_md5" json:"name_md5"`
	//IsEnCrypt bool   `gorm:"column:is_encrypt" json:"is_encrypt"` //是否已经编写了加密代码，编写了才可以继续编写解密代码
	//IsSolved  bool   `gorm:"column:is_solved" json:"is_solved"`
}

type Challenge struct {
	ID          int    `gorm:"primaryKey" json:"id"`
	Title       string `gorm:"column:title" json:"title"`
	Description string `gorm:"column:description" json:"description"`
	Data        string `gorm:"column:data" json:"-"` //data固定需要选手提取与写入内容，存放内容格式为123,456,789
}

type UserChallenge struct {
	ID          int  `gorm:"primaryKey" json:"id"`
	UserID      int  `gorm:"column:user_id" json:"user_id"`
	ChallengeID int  `gorm:"column:challenge_id" json:"challenge_id"`
	IsEnCrypt   bool `gorm:"column:is_encrypt" json:"is_encrypt"`
	IsSolved    bool `gorm:"column:is_solved" json:"is_solved"`
}

//提交记录
type SubmitRecord struct {
	ID          int           `gorm:"primaryKey" json:"id"`
	UserID      int           `gorm:"column:user_id" json:"user_id"`
	ChallengeID int           `gorm:"column:challenge_id" json:"challenge_id"`
	SubmitTime  time.Time     `gorm:"column:submit_time" json:"submit_time"`
	Language    string        `gorm:"column:language" json:"language"`
	EncryptCode string        `gorm:"column:encrypt_code" json:"encrypt_code"`
	DecryptCode string        `gorm:"column:decrypt_code" json:"decrypt_code"`
	Status      int           `gorm:"column:status" json:"status"` //内容见submit\type.go
	Memory      uint64        `gorm:"column:memory" json:"memory"`
	RunTime     time.Duration `gorm:"column:run_time" json:"run_time"`
}
