package database

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
)

var ormDB *gorm.DB

func InitDB() (err error) {
	ormDB, err = gorm.Open(sqlite.Open("sql.db"), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			SingularTable: true, // 使用单数表名
		},
	})
	ormDB.AutoMigrate(&User{}, &SubmitRecord{}, &Challenge{}, &UserChallenge{})
	if err != nil {
		panic("failed to connect database")
	}
	return
}

func GetDB() (*gorm.DB, error) {
	var err error
	if ormDB == nil {
		err = InitDB()
	}
	return ormDB, err
}
