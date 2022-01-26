# Git分支管理

时间线是Git的分支，称为主分支`master`,`HEAD`指向`master`，`master`指向提交，`HEAD`指向当前分支

每次提交，`master`分支都会向前移动一步，这样，随着你不断提交，`master`分支的线也越来越长。

当我们创建新的分支，例如`dev`时，Git新建了一个指针叫`dev`，指向`master`相同的提交，再把`HEAD`指向`dev`，就表示当前分支在`dev`上：

创建分支命令：

```
git branch(branchname)
```



![git-br-initial](https://www.liaoxuefeng.com/files/attachments/919022325462368/0)