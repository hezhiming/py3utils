
## 自动执行UT

UT 和 Lint 工具的检查，对于Python这种动态语言，是必不可少的。

所以最好在每次push到远程仓库时，都自动执行对应的动作，这个我们可以使用 git hooks 做，步骤如下：
1. cd "THE PROJECT HOME"
2. vim .git/hooks/pre-push
3. 添加如下内容
```
./run_pytest_and_pylint.sh
```


## 手动执行UT
当然也可以手动去做这件事情，步骤如下：
1. 进入到项目主目录，cd "PROJECT HOME"
2. 运行如下命令：source run_pytest_and_pylint.sh