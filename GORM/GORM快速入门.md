# GORM快速入门

```go
package main

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Code  string
	Price uint //不带符号
}

func main() {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{}) //连接数据库，并将sql文件导入
	if err != nil {
		panic("failed to connect database")
	} //c处理错误
	//迁移schema
	db.AutoMigrate(&Product{})

	//创建新内容
	db.Create(&Product{Code: "D42", Price: 100})
	//读取
	var product Product
	db.First(&product, 1)               //根据整型的主键查找
	db.First(&product, "code=?", "D42") //查找code字段值为D42的记录

	//更新值
	db.Model(&product).Update("Price", 200)
	//更新多个字段
	db.Model(&product).Updates(Product{Price: 200, Code: "F42"})
	//仅更新非0字段
	db.Model(&product).Updates(map[string]interface{}{"Price": 200, "Code": "F42"})
	//Delete - 删除Product
	db.Delete(&product, 1)
}

```

