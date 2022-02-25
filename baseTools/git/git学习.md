git学习笔记

一、git安装：

linux（已Ubuntu为例）

安装git：

1、查看git有无安装：命令 git

2、git安装：sudo apt-get install git

3、已安装的git版本升级``

   >先升级一个git源： sudo add-apt-repository ppa:git-core/ppa
> 
   >更新安装列表：sudo apt-get update
> 
> 升级git：sudo apt-get install git
> 
  windows（安装）

下载git可执行文件，一路点击下一步

安装完成后执行（配置角色）

 >cmd启动窗口 ： git config --global user.name "your name"
    git config --global user.email "your email"
> 
二、创建版本库
>首先创建一个目录文件夹，用来存放git项目文件
> 
> 在这个文件夹下右键打开git bash 输入命令git init 实现初始化项目，创建一个属于该项目独有的仓库（repository）
> 
> 添加文件到版本库   git add (后面可跟文件名，或者.)
> 
> 文件提交到版本库   git commit -m "提交的别名，方便识别"
> 
三、版本命令及场景
> 查看版本历史   git log  按照提交时间倒序排列，最近提交的在上面， 嫌弃输入内容太多可以使用 git log  --pretty=oneline
> 
> 当前版本的是HEAD  返回上一个版本就是  git reset --hard HEAD^  ,返回很久之前版本  git rest --hard HEAD~8  返回之前8个版本
> 
> 回到未来的某个版本  git reset --hard 1094a  ,如果找不到未来的某个版本id，可以通过git reflog查看
> 
> 
> 
HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。

要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

工作区、暂存区（每次添加修改都是放到暂存区，提交就是将暂存区的提交）

>git diff HEAD --readme.txt 查看提交的不同点
> 
> git status 查看当前状态
> 
> git checkout --readme.txt 丢弃当前修改 （如果不加文件，就成了切换分支）
> 
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD <file>，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

四、远程仓库

场景1：你已经在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步，这样，GitHub上的仓库既可以作为备份，又可以让其他人通过该仓库来协作，真是一举多得。

操作步骤：

首先，登陆GitHub，然后，在右上角找到“Create a new repo”按钮，创建一个新的仓库：
在Repository name填入learngit，其他保持默认设置，点击“Create repository”按钮，就成功地创建了一个新的Git仓库：
目前，在GitHub上的这个learngit仓库还是空的，GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

`$ git remote add origin git@github.com:michaelliao/learngit.git`

删除远程库：

`$ git remote -v  查看远程库信息
origin  git@github.com:michaelliao/learn-git.git (fetch)
origin  git@github.com:michaelliao/learn-git.git (push)`

`$ git remote rm origin`

此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除

克隆远程库：

git clone + 地址


五、分支管理

有一条主线：主分支（master）  HEAD指针指向的其实就是master分支

创建分支：
> git checkout -b dev  创建dev分支 -b表示创建分支并切换到分支
> 
> git branch  查看当前分支
> 
> git checkout master  切换到master分支
> 
> git merge dev  将dev分支合并到master分支上
> 
> git branch -d dev  删除dev分支
>
> git switch master 切换到master分支 Switch使用更加科学
> 
> 
解决冲突：

产生原因：两个分支上对某个文件都有修改，合并分支会出冲突，只能先解决二者问题，在合并

查看分支合并情况：

>git log --graph --pretty=oneline --abbrev-commit
> 
分支策略

>在实际开发中，我们应该按照几个基本原则进行分支管理：
> 
>首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；

>那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；

>你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。`
   