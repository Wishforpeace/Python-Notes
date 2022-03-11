# go项目部署到linxu

2020-09-27阅读 4390

环境: 在mac上编译, 编译后上传到linux, 然后运行代码

**go项目打包**

一、直接部署到linux

\1. 在mac上, 进入到项目目录, 执行以下命令, 进行编译: CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go, 生成一个main文件. 

\2. 将main文件上传到linux任意目录下, 执行 nohup ./main &运行项目. 如果出错, 则查看日志即可

二. 通过nginx部署

 **beego项目打包**

 环境: 本地开发是mac, 部署到linux

\1. 在mac上, 进入到项目目录, 执行: bee pack -be GOOS=linux 进行打包, 打包成功后, 会生成一个****.tar.gz的文件.

\2. 在linux的某一个目录下创建一个新的文件夹(一定要创建, 否则会解压到根目录), 将***tar.gz文件上传到linux. 

\3. 解压 tar -xvzf xxxx.tar.gz

\4. 分配权限: sudo chmod 777 xxxx

\5. 运行可执行文件. nohup ./**** &  成功