# Belongs To

## Belongs To

`belongs to`与另外一个模型建立一对一连接，这种模型每个实例都属于另一个模型的实例

```go
type User struct {
	gorm.Model
	Name string
	CompanyID int
	Company Company
}

type Company struct {
	ID int
	Name string
}
//User属于Company，CompanyID是外键
```

## 重写外键

定义`belongs to`,必须存在外键

自定义外键

```go
type User struct {
	gorm.Model
	Name         string
	CompanyRefer int
	Company      Company 'gorm:"foreignKey:CompanyRefer"'
	//使用CompanyRefer 作为外键
}

type Company struct {
	ID   int
	Name string
}
```

# 重写引用

`GORM`经常使用拥有者的主字段作为外键的值。对于上面的例子，它是`Company` 的`ID`字段

```go
type User struct {
	gorm.Model
	Name      string
	CompanyID string
	Company   Company 'gorm:"references:Code"'
	//使用Code作为引用
}

type Company struct {
	ID   int
	Code string
	Name string
}
```

## Belongs to 的CRUD

查看 [关联模式](https://learnku.com/docs/gorm/v2/associations#Association-Mode) 获取 belongs to 相关的用法

## 预加载

通过`Preload` `Joins`预加载belongs to 关联的记录

