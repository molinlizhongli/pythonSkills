场景1：加入远程仓库，拉取仓库代码
> 连接远程仓库：git remote add origin git@github.com:michaelliao/learngit.git
> 
> 克隆代码到本地：git clone git@github.com:michaelliao/learngit.git
> 
场景2： 将本地目录改为git项目并传到远程仓库
> 本地目录初始化：git init
> 
> 添加所有文件  git add.
> 
> 提交文件：git commit -m "init"
> 
> 创建主分支： git branch -M main
> 
> 连接远程仓库（提前建立一个空的）git remote add origin https://github.com/molin/test.git
> 
> 推送代码到仓库： git push -u origin main
> 
场景3：推送一个已经存在的仓库到远程仓库
> 连接远程仓库： git remote add origin https://github.com/molin/test.git
> 
> 创建主分支： git branch -M main
> 
> 推送代码到仓库： git push -u origin main