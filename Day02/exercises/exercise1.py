Today  I am doing some exercise about git
The steps are as fellowed
*Task00
创建目录(git_test019)并在目录下打开gitbash
git init#初始化git仓库

*Task01
touch file01.txt#目录下创建file01.txt
git add.#将修改加入暂存区
将修改提交到本地仓库，提交记录内容为：commit 01
查看日志


*Task02
修改file01的内容为：每天快乐学习
将修改加入暂存区
将修改提交到本地仓库，提交记录内容为：practice makes good
查看日志
以精简的方式显示提交目录

*Task03
查看提交记录
找到倒数第二次提交的commitID
版本回退

Code

my vlog：
step01 open terminal

*Task00
mkdir git_test02#建立文件夹git_test02
cd git_test02#打开文件夹所在目录
"D:\2024new software\Git\git-bash.exe"打开所在目录的gitbash
git init初始化git仓库

*Task01#创建你文件并提交
touch file01.txt
git add .
git log

*Task02#修改文件并提交
vi file01.txt
git add .
git commit -m'commit02'
git log

*Task03#以精简的方式显示提交记录
alias git-log='git log --pretty=oneline --all --graph --abbrev-commit'
git - log

*Task04#版本回退
git reset --hard d5555d8
git-log
git reset --hard abfafef
git - log

*Task05#查看日志历史记录
git reflog

*Task06#创建一个无需git管理的文件内，并把需要的文件放入
touch file.a
touch .gitignore
vi.gitignore#:*.a
git status



