# Git的四个工作区域

四个工作区域：工作目录（Working Directory）、暂存区（Stage/Index），资源库（Repository）、git仓库（Remote Directory）

![img](https://img2018.cnblogs.com/blog/1090617/201810/1090617-20181008211557402-232838726.png)

+ **Workspace**：工作区，平时存储代码的地方
+ **Index/Stage**：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信
+ **Repository**：仓库区，就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本。
+ **Remote**：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑中用于远程数据交换