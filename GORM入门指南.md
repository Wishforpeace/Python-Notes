# 入门指南

## 特性

- 全功能 ORM

- 关联 (Has One，Has Many，Belongs To，Many To Many，多态，单表继承)

- Create，Save，Update，Delete，Find 中钩子方法

- 支持 `Preload`、`Joins` 的预加载

- 事务，嵌套事务，Save Point，Rollback To Saved Point

- Context、预编译模式、DryRun 模式

- 批量插入，FindInBatches，Find/Create with Map，使用 SQL 表达式、Context Valuer 进行 CRUD

- SQL 构建器，Upsert，数据库锁，Optimizer/Index/Comment Hint，命名参数，子查询

- 复合主键，索引，约束

- Auto Migration

- 自定义 Logger

- 灵活的可扩展插件 API：Database Resolver（多数据库，读写分离）、Prometheus…

- 每个特性都经过了测试的重重考验

- 开发者友好

- ### 安装

  ```
  go get -u gorm.io/gorm
  go get -u gorm.io/driver/sqlite
  ```

  #### 快速入门

  ```go
  package main
  
  import (
    "gorm.io/gorm"
    "gorm.io/driver/sqlite"
  )
  
  type Product struct {
    gorm.Model
    Code  string
    Price uint
  }
  
  func main() {
    db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
    if err != nil {
      panic("failed to connect database")
    }
  
    // 迁移 schema
    db.AutoMigrate(&Product{})
  
    // Create
    db.Create(&Product{Code: "D42", Price: 100})
  
    // Read
    var product Product
    db.First(&product, 1) // 根据整形主键查找
    db.First(&product, "code = ?", "D42") // 查找 code 字段值为 D42 的记录
  
    // Update - 将 product 的 price 更新为 200
    db.Model(&product).Update("Price", 200)
    // Update - 更新多个字段
    db.Model(&product).Updates(Product{Price: 200, Code: "F42"}) // 仅更新非零值字段
    db.Model(&product).Updates(map[string]interface{}{"Price": 200, "Code": "F42"})
  
    // Delete - 删除 product
    db.Delete(&product, 1)
  }
  ```

  

## 模型定义

### 模型定义

模型是标准的 struct，由 Go 的基本数据类型、实现了 [Scanner](https://pkg.go.dev/database/sql/?tab=doc#Scanner) 和 [Valuer](https://pkg.go.dev/database/sql/driver#Valuer) 接口的自定义类型及其指针或别名组成

例如：

```go
type User struct {
  ID           uint
  Name         string
  Email        *string
  Age          uint8
  Birthday     *time.Time
  MemberNumber sql.NullString
  ActivatedAt  sql.NullTime
  CreatedAt    time.Time
  UpdatedAt    time.Time
}
```

#### 约定

+ GORM倾向于约定，而不是配置。
+ 默认情况下，GORM 使用 `ID` 作为主键，使用结构体名的 `蛇形复数` 作为表名，字段名的 `蛇形` 作为列名，并使用 `CreatedAt`、`UpdatedAt` 字段追踪创建、更新时间
+ 遵循 GORM 已有的约定，可以减少您的配置和代码量。如果约定不符合您的需求，[GORM 允许您自定义配置它们](https://gorm.io/zh_CN/docs/conventions.html)

#### Gorm.Model

GORM定义一个`gorm.Model`结构体，其包括字段`ID` `CreateAt ` ` UpdateAt` `DeleteAt`

```go
// gorm.Model 的定义
type Model struct {
  ID        uint           `gorm:"primaryKey"`
  CreatedAt time.Time
  UpdatedAt time.Time
  DeletedAt gorm.DeletedAt `gorm:"index"`
}
```

您可以将它嵌入到您的结构体中，以包含这几个字段，详情请参考 [嵌入结构体](https://gorm.io/zh_CN/docs/models.html#embedded_struct)

### 高级选项

#### 字段级权限控制

可导出的字段在使用 GORM 进行 CRUD 时拥有全部的权限，此外，GORM 允许您用标签控制字段级别的权限。这样您就可以让一个字段的权限是只读、只写、只创建、只更新或者被忽略

> **注意：** 使用 GORM Migrator 创建表时，不会创建被忽略的字段

```go
type User struct{
	Name string `gorm:"<-:create"`//允许读和创建
	Name string `gorm:"<-:update"`//允许读和更新
	Name string `gorm:"<-"`//允许读和写（创新和更新）
	Name string `gorm:"<-:false"`//允许读，禁止写
	Name string `gorm:"->"`//只读（除非有自定义配置，否则禁止写
	Name string `gorm:"->;<-create"`//允许读和写
	Name string `gorm:"->:false;<-:create"`//仅创建（禁止从db读）
	Name string `gorm:"-"`//通过struct读写会忽略该字段
}
```

#### 创建/更新时间追踪（纳秒、毫秒、秒、Time）

GORM 约定使用 `CreatedAt`、`UpdatedAt` 追踪创建/更新时间。如果您定义了这种字段，GORM 在创建、更新时会自动填充 [当前时间](https://gorm.io/zh_CN/docs/gorm_config.html#now_func)

要使用不同名称的字段，您可以配置 `autoCreateTime`、`autoUpdateTime` 标签

如果您想要保存 UNIX（毫/纳）秒时间戳，而不是 time，您只需简单地将 `time.Time` 修改为 `int` 即可

```go
type User struct {
  CreatedAt time.Time // Set to current time if it is zero on creating
  UpdatedAt int       // Set to current unix seconds on updating or if it is zero on creating
  Updated   int64 `gorm:"autoUpdateTime:nano"` // Use unix nano seconds as updating time
  Updated   int64 `gorm:"autoUpdateTime:milli"`// Use unix milli seconds as updating time
  Created   int64 `gorm:"autoCreateTime"`      // Use unix seconds as creating time
}
```

#### 嵌入结构体

对于匿名字段，GORM会将其字段包含在父结构体中，例如：

```go
type User struct {  gorm.Model  Name string}// 等效于
type User struct {  
  ID        uint           `gorm:"primaryKey"`  
  CreatedAt time.Time  
  UpdatedAt time.Time  
  DeletedAt gorm.DeletedAt `gorm:"index"`  
  Name string
}
```

对于正常的结构体字段，你也可以通过标签`embedded`将其嵌入，例如：

```go
type Author struct {
    Name  string
    Email string
}

type Blog struct {
  ID      int
  Author  Author `gorm:"embedded"`
  Upvotes int32
}
// 等效于
type Blog struct {
  ID    int64
  Name  string
  Email string
  Upvotes  int32
}
```

并且，您可以使用标签 `embeddedPrefix` 来为 db 中的字段名添加前缀，例如：

```go
type Blog struct {
  ID      int
  Author  Author `gorm:"embedded;embeddedPrefix:author_"`
  Upvotes int32
}
// 等效于
type Blog struct {
  ID          int64
    AuthorName  string
    AuthorEmail string
  Upvotes     int32
}
```

#### 字段标签

声明 model 时，tag 是可选的，GORM 支持以下 tag： tag 名大小写不敏感，但建议使用 `camelCase` 风格

| 标签名                 | 说明                                                         |
| :--------------------- | :----------------------------------------------------------- |
| column                 | 指定 db 列名                                                 |
| type                   | 列数据类型，推荐使用兼容性好的通用类型，例如：所有数据库都支持 bool、int、uint、float、string、time、bytes 并且可以和其他标签一起使用，例如：`not null`、`size`, `autoIncrement`… 像 `varbinary(8)` 这样指定数据库数据类型也是支持的。在使用指定数据库数据类型时，它需要是完整的数据库数据类型，如：`MEDIUMINT UNSIGNED not NULL AUTO_INCREMENT` |
| size                   | 指定列大小，例如：`size:256`                                 |
| primaryKey             | 指定列为主键                                                 |
| unique                 | 指定列为唯一                                                 |
| default                | 指定列的默认值                                               |
| precision              | 指定列的精度                                                 |
| scale                  | 指定列大小                                                   |
| not null               | 指定列为 NOT NULL                                            |
| autoIncrement          | 指定列为自动增长                                             |
| autoIncrementIncrement | 自动步长，控制连续记录之间的间隔                             |
| embedded               | 嵌套字段                                                     |
| embeddedPrefix         | 嵌入字段的列名前缀                                           |
| autoCreateTime         | 创建时追踪当前时间，对于 `int` 字段，它会追踪秒级时间戳，您可以使用 `nano`/`milli` 来追踪纳秒、毫秒时间戳，例如：`autoCreateTime:nano` |
| autoUpdateTime         | 创建/更新时追踪当前时间，对于 `int` 字段，它会追踪秒级时间戳，您可以使用 `nano`/`milli` 来追踪纳秒、毫秒时间戳，例如：`autoUpdateTime:milli` |
| index                  | 根据参数创建索引，多个字段使用相同的名称则创建复合索引，查看 [索引](https://gorm.io/zh_CN/docs/indexes.html) 获取详情 |
| uniqueIndex            | 与 `index` 相同，但创建的是唯一索引                          |
| check                  | 创建检查约束，例如 `check:age > 13`，查看 [约束](https://gorm.io/zh_CN/docs/constraints.html) 获取详情 |
| <-                     | 设置字段写入的权限， `<-:create` 只创建、`<-:update` 只更新、`<-:false` 无写入权限、`<-` 创建和更新权限 |
| ->                     | 设置字段读的权限，`->:false` 无读权限                        |
| -                      | 忽略该字段，`-` 无读写权限                                   |
| comment                | 迁移时为字段添加注释                                         |

#### 关联标签

GORM 允许通过标签为关联配置外键、约束、many2many 表，详情请参考 [关联部分](https://gorm.io/zh_CN/docs/associations.html#tags)

## 连接到数据库

### MySQL

```go
import (
  "gorm.io/driver/mysql"
  "gorm.io/gorm"
)

func main() {
  // 参考 https://github.com/go-sql-driver/mysql#dsn-data-source-name 获取详情
    dsn := "user:pass@tcp(127.0.0.1:3306)/dbname?charset=utf8mb4&parseTime=True&loc=Local"
    db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
}
```

>  **注意：**想要正确的处理 `time.Time` ，您需要带上 `parseTime` 参数， ([更多参数](https://github.com/go-sql-driver/mysql#parameters)) 要支持完整的 UTF-8 编码，您需要将 `charset=utf8` 更改为 `charset=utf8mb4` 查看 [此文章](https://mathiasbynens.be/notes/mysql-utf8mb4) 获取详情

MySQl 驱动程序提供了 [一些高级配置](https://github.com/go-gorm/mysql) 可以在初始化过程中使用，例如：

```go
db, err := gorm.Open(mysql.New(mysql.Config{
  DSN: "gorm:gorm@tcp(127.0.0.1:3306)/gorm?charset=utf8&parseTime=True&loc=Local", // DSN data source name
  DefaultStringSize: 256, // string 类型字段的默认长度
  DisableDatetimePrecision: true, // 禁用 datetime 精度，MySQL 5.6 之前的数据库不支持
  DontSupportRenameIndex: true, // 重命名索引时采用删除并新建的方式，MySQL 5.7 之前的数据库和 MariaDB 不支持重命名索引
  DontSupportRenameColumn: true, // 用 `change` 重命名列，MySQL 8 之前的数据库和 MariaDB 不支持重命名列
  SkipInitializeWithVersion: false, // 根据当前 MySQL 版本自动配置
}), &gorm.Config{})
```

### 自定义驱动

GORM 允许通过 `DriverName` 选项自定义 MySQL 驱动，例如：

```go
import (
  _ "example.com/my_mysql_driver"
  "gorm.io/gorm"
)

db, err := gorm.Open(mysql.New(mysql.Config{
  DriverName: "my_mysql_driver",
  DSN: "gorm:gorm@tcp(localhost:9910)/gorm?charset=utf8&parseTime=True&loc=Local", // Data Source Name，参考 https://github.com/go-sql-driver/mysql#dsn-data-source-name
}), &gorm.Config{})
```

### 现有的数据库连接

GORM 允许通过一个现有的数据库连接来初始化 `*gorm.DB`

```go
import (
  "database/sql"
  "gorm.io/driver/mysql"
  "gorm.io/gorm"
)

sqlDB, err := sql.Open("mysql", "mydb_dsn")
gormDB, err := gorm.Open(mysql.New(mysql.Config{
  Conn: sqlDB,
}), &gorm.Config{})
```

## PostgreSQL

```go
import (
  "gorm.io/driver/postgres"
  "gorm.io/gorm"
)

dsn := "host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai"
db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
```

我们使用 [pgx](https://github.com/jackc/pgx) 作为 postgres 的 database/sql 驱动，默认情况下，它会启用 prepared statement 缓存，你可以这样禁用它：

```go
// https://github.com/go-gorm/postgres
db, err := gorm.Open(postgres.New(postgres.Config{
  DSN: "user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai",
  PreferSimpleProtocol: true, // disables implicit prepared statement usage
}), &gorm.Config{})
```

### 自定义驱动

GORM 允许通过 `DriverName` 选项自定义 PostgreSQL 驱动，例如：

```go
import (
  _ "github.com/GoogleCloudPlatform/cloudsql-proxy/proxy/dialers/postgres"
  "gorm.io/gorm"
)

db, err := gorm.Open(postgres.New(postgres.Config{
  DriverName: "cloudsqlpostgres",
  DSN: "host=project:region:instance user=postgres dbname=postgres password=password sslmode=disable",
})
```

### 现有的数据库连接

GORM 允许通过一个现有的数据库连接来初始化 `*gorm.DB`

```go
import (
  "database/sql"
  "gorm.io/driver/postgres"
  "gorm.io/gorm"
)

sqlDB, err := sql.Open("postgres", "mydb_dsn")
gormDB, err := gorm.Open(postgres.New(postgres.Config{
  Conn: sqlDB,
}), &gorm.Config{})
```

## SQLite

```go
import (
  "gorm.io/driver/sqlite"
  "gorm.io/gorm"
)

// github.com/mattn/go-sqlite3
db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})
```

> **注意：** 您也可以使用 `file::memory:?cache=shared` 替代文件路径。 这会告诉 SQLite 在系统内存中使用一个临时数据库。 (查看 [SQLite 文档](https://www.sqlite.org/inmemorydb.html) 获取详情)

## SQL Server

```go
import (
  "gorm.io/driver/sqlserver"
  "gorm.io/gorm"
)

// github.com/denisenkom/go-mssqldb
dsn := "sqlserver://gorm:LoremIpsum86@localhost:9930?database=gorm"
db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{})
```

## Clickhouse

https://github.com/go-gorm/clickhouse

```go
import (
  "gorm.io/driver/clickhouse"
  "gorm.io/gorm"
)

func main() {
  dsn := "tcp://localhost:9000?database=gorm&username=gorm&password=gorm&read_timeout=10&write_timeout=20"
  db, err := gorm.Open(clickhouse.Open(dsn), &gorm.Config{})

  // Auto Migrate
  db.AutoMigrate(&User{})
  // Set table options
  db.Set("gorm:table_options", "ENGINE=Distributed(cluster, default, hits)").AutoMigrate(&User{})

  // 插入
  db.Create(&user)

  // 查询
  db.Find(&user, "id = ?", 10)

  // 批量插入
  var users = []User{user1, user2, user3}
  db.Create(&users)
  // ...
}
```

## 连接池

GORM 使用 [database/sql](https://pkg.go.dev/database/sql) 维护连接池

```go
sqlDB, err := db.DB()

// SetMaxIdleConns 设置空闲连接池中连接的最大数量
sqlDB.SetMaxIdleConns(10)

// SetMaxOpenConns 设置打开数据库连接的最大数量。
sqlDB.SetMaxOpenConns(100)

// SetConnMaxLifetime 设置了连接可复用的最大时间。
sqlDB.SetConnMaxLifetime(time.Hour)
```

查看 [通用接口](https://gorm.io/zh_CN/docs/generic_interface.html) 获取详情。

## 不支持的数据库

有些数据库可能兼容 `mysql`、`postgres` 的方言，在这种情况下，你可以直接使用这些数据库的方言。

对于其它不支持的数据，[我们鼓励且欢迎大家伙开发更多数据库类型的驱动！](https://gorm.io/zh_CN/docs/write_driver.html)

# CRUD接口

## 创建

### 用指定的字段创建记录

创建记录并更新给出的字段。

```go
db.Select("Name", "Age", "CreatedAt").Create(&user)
// INSERT INTO `users` (`name`,`age`,`created_at`) VALUES ("jinzhu", 18, "2020-07-04 11:05:21.775")
```

创建一个记录且一同忽略传递给略去的字段值。

```go
db.Omit("Name", "Age", "CreatedAt").Create(&user)
// INSERT INTO `users` (`birthday`,`updated_at`) VALUES ("2020-01-01 00:00:00.000", "2020-07-04 11:05:21.775")
```

### 批量插入

要有效地插入大量记录，请将一个 `slice` 传递给 `Create` 方法。 GORM 将生成单独一条SQL语句来插入所有数据，并回填主键的值，钩子方法也会被调用。

```go
var users = []User{{Name: "jinzhu1"}, {Name: "jinzhu2"}, {Name: "jinzhu3"}}
db.Create(&users)

for _, user := range users {
  user.ID // 1,2,3
}
```

使用 `CreateInBatches` 分批创建时，你可以指定每批的数量，例如：

```go
var users = []User{{name: "jinzhu_1"}, ...., {Name: "jinzhu_10000"}}

// 数量为 100
db.CreateInBatches(users, 100)
```

[Upsert](https://gorm.io/zh_CN/docs/create.html#upsert) 和 [Create With Associations](https://gorm.io/zh_CN/docs/create.html#create_with_associations) 也支持批量插入

> **注意** 使用`CreateBatchSize` 选项初始化 GORM 时，所有的创建& 关联 `INSERT` 都将遵循该选项

```go
db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{
  CreateBatchSize: 1000,
})

db := db.Session(&gorm.Session{CreateBatchSize: 1000})

users = [5000]User{{Name: "jinzhu", Pets: []Pet{pet1, pet2, pet3}}...}

db.Create(&users)
// INSERT INTO users xxx (5 batches)
// INSERT INTO pets xxx (15 batches)
```

### 创建钩子

GORM 允许用户定义的钩子有 `BeforeSave`, `BeforeCreate`, `AfterSave`, `AfterCreate` 创建记录时将调用这些钩子方法，请参考 [Hooks](https://gorm.io/zh_CN/docs/hooks.html) 中关于生命周期的详细信息

```go
func (u *User) BeforeCreate(tx *gorm.DB) (err error) {
  u.UUID = uuid.New()

    if u.Role == "admin" {
        return errors.New("invalid role")
    }
    return
}
```

如果您想跳过 `钩子` 方法，您可以使用 `SkipHooks` 会话模式，例如：

```go
DB.Session(&gorm.Session{SkipHooks: true}).Create(&user)

DB.Session(&gorm.Session{SkipHooks: true}).Create(&users)

DB.Session(&gorm.Session{SkipHooks: true}).CreateInBatches(users, 100)
```

### 根据 Map 创建

GORM 支持根据 `map[string]interface{}` 和 `[]map[string]interface{}{}` 创建记录，例如：

```go
db.Model(&User{}).Create(map[string]interface{}{
  "Name": "jinzhu", "Age": 18,
})

// batch insert from `[]map[string]interface{}{}`
db.Model(&User{}).Create([]map[string]interface{}{
  {"Name": "jinzhu_1", "Age": 18},
  {"Name": "jinzhu_2", "Age": 20},
})
```

> **注意：** 根据 map 创建记录时，association 不会被调用，且主键也不会自动填充

### 使用 SQL 表达式、Context Valuer 创建记录

GORM 允许使用 SQL 表达式插入数据，有两种方法实现这个目标。根据 `map[string]interface{}` 或 [自定义数据类型](https://gorm.io/zh_CN/docs/data_types.html#gorm_valuer_interface) 创建，例如：

```go
// 通过 map 创建记录
db.Model(User{}).Create(map[string]interface{}{
  "Name": "jinzhu",
  "Location": clause.Expr{SQL: "ST_PointFromText(?)", Vars: []interface{}{"POINT(100 100)"}},
})
// INSERT INTO `users` (`name`,`location`) VALUES ("jinzhu",ST_PointFromText("POINT(100 100)"));

// 通过自定义类型创建记录
type Location struct {
    X, Y int
}

// Scan 方法实现了 sql.Scanner 接口
func (loc *Location) Scan(v interface{}) error {
  // Scan a value into struct from database driver
}

func (loc Location) GormDataType() string {
  return "geometry"
}

func (loc Location) GormValue(ctx context.Context, db *gorm.DB) clause.Expr {
  return clause.Expr{
    SQL:  "ST_PointFromText(?)",
    Vars: []interface{}{fmt.Sprintf("POINT(%d %d)", loc.X, loc.Y)},
  }
}

type User struct {
  Name     string
  Location Location
}

db.Create(&User{
  Name:     "jinzhu",
  Location: Location{X: 100, Y: 100},
})
// INSERT INTO `users` (`name`,`location`) VALUES ("jinzhu",ST_PointFromText("POINT(100 100)"))
```

### 高级选项

#### 关联创建

创建关联数据时，如果关联值是非零值，这些关联会被 upsert，且它们的 `Hook` 方法也会被调用

```go
type CreditCard struct {
  gorm.Model
  Number   string
  UserID   uint
}

type User struct {
  gorm.Model
  Name       string
  CreditCard CreditCard
}

db.Create(&User{
  Name: "jinzhu",
  CreditCard: CreditCard{Number: "411111111111"}
})
// INSERT INTO `users` ...
// INSERT INTO `credit_cards` ...
```

您也可以通过 `Select`、 `Omit` 跳过关联保存，例如：

```go
db.Omit("CreditCard").Create(&user)

// 跳过所有关联
db.Omit(clause.Associations).Create(&user)
```

#### 默认值

您可以通过标签 `default` 为字段定义默认值，如：

```go
type User struct {
  ID   int64
  Name string `gorm:"default:galeone"`
  Age  int64  `gorm:"default:18"`
}
```

插入记录到数据库时，默认值 *会被用于* 填充值为 [零值](https://tour.golang.org/basics/12) 的字段

> **注意** 对于声明了默认值的字段，像 `0`、`''`、`false` 等零值是不会保存到数据库。您需要使用指针类型或 Scanner/Valuer 来避免这个问题，例如：

```
type User struct {
  gorm.Model
  Name string
  Age  *int           `gorm:"default:18"`
  Active sql.NullBool `gorm:"default:true"`
}
```

> **注意** 若要数据库有默认、虚拟/生成的值，你必须为字段设置 `default` 标签。若要在迁移时跳过默认值定义，你可以使用 `default:(-)`，例如：

```
type User struct {
  ID        string `gorm:"default:uuid_generate_v3()"` // db func
  FirstName string
  LastName  string
  Age       uint8
  FullName  string `gorm:"->;type:GENERATED ALWAYS AS (concat(firstname,' ',lastname));default:(-);"`
}
```

使用虚拟/生成的值时，你可能需要禁用它的创建、更新权限，查看 [字段级权限](https://gorm.io/zh_CN/docs/models.html#field_permission) 获取详情

#### Upsert 及冲突

GORM 为不同数据库提供了兼容的 Upsert 支持

```go
import "gorm.io/gorm/clause"

// 在冲突时，什么都不做
db.Clauses(clause.OnConflict{DoNothing: true}).Create(&user)

// 在`id`冲突时，将列更新为默认值
db.Clauses(clause.OnConflict{
  Columns:   []clause.Column{{Name: "id"}},
  DoUpdates: clause.Assignments(map[string]interface{}{"role": "user"}),
}).Create(&users)
// MERGE INTO "users" USING *** WHEN NOT MATCHED THEN INSERT *** WHEN MATCHED THEN UPDATE SET ***; SQL Server
// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE ***; MySQL

// 使用SQL语句
db.Clauses(clause.OnConflict{
  Columns:   []clause.Column{{Name: "id"}},
  DoUpdates: clause.Assignments(map[string]interface{}{"count": gorm.Expr("GREATEST(count, VALUES(count))")}),
}).Create(&users)
// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE `count`=GREATEST(count, VALUES(count));

// 在`id`冲突时，将列更新为新值
db.Clauses(clause.OnConflict{
  Columns:   []clause.Column{{Name: "id"}},
  DoUpdates: clause.AssignmentColumns([]string{"name", "age"}),
}).Create(&users)
// MERGE INTO "users" USING *** WHEN NOT MATCHED THEN INSERT *** WHEN MATCHED THEN UPDATE SET "name"="excluded"."name"; SQL Server
// INSERT INTO "users" *** ON CONFLICT ("id") DO UPDATE SET "name"="excluded"."name", "age"="excluded"."age"; PostgreSQL
// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE `name`=VALUES(name),`age=VALUES(age); MySQL

// 在冲突时，更新除主键以外的所有列到新值。
db.Clauses(clause.OnConflict{
  UpdateAll: true,
}).Create(&users)
// INSERT INTO "users" *** ON CONFLICT ("id") DO UPDATE SET "name"="excluded"."name", "age"="excluded"."age", ...;
```

您还可以查看 [高级查询](https://gorm.io/zh_CN/docs/advanced_query.html) 中的 `FirstOrInit`、`FirstOrCreate`

查看 [原生 SQL 及构造器](https://gorm.io/zh_CN/docs/sql_builder.html) 获取更多细节