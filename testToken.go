package main

import (
	"fmt"
	jsoniter "github.com/json-iterator/go"
	"io/ioutil"
	"net/http"
)

//https://flagserver.wm-team.cn/getFlag?uuid=fa1c7bea-b769-4520-87a1-5e0f0112b98c&teamtoken=fffffffffffff&teamname=yyy

//https://flagserver.wm-team.cn/exist?uuid=fa1c7bea-b769-4520-87a1-5e0f0112b98c&teamtoken=fffffffffffff&teamname=yyy

var url = "https://flagserver.wm-team.cn/exist?uuid=fa1c7bea-b769-4520-87a1-5e0f0112b98c&teamtoken="

var jsonnew = jsoniter.ConfigCompatibleWithStandardLibrary

func IsTokenValid(token string) bool {
	resp, err := http.Get(url + token)
	if err != nil {
		return false
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	data := jsonnew.Get(body)
	if data.Get("data").ToBool() == true {
		return true
	} else {
		return false
	}

}

func main() {
	fmt.Print(IsTokenValid("fffffffffffff"))
}
