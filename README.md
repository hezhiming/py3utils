# py3utils: Useful Python 3 utils

Some useful Python 3 utils.

## Why
如果你和我一样，深入使用过 Python，但是对标准库由种种不满。比如，你认同这些观点：
* Python 的标准数据结构设计得非常好，API 简洁而且优雅。
* 但是 Python 的某些标准库却是比较混乱，API 及其不友好。
* 尽管现在“函数式编程”很火，但是“面向对象”仍然是管理复杂软件的最好的编程手段，因为它可以显著地降低人脑负担。同时，设计模式也是值得学习的知识。

那么，你大概率会喜欢这个库。

这个库做了一些很简单的事情，比如：
* 将某些标准库的 API 做简单的包装，使其更加容易记忆。
* 尽量对外提供 class，以面向对象的方式提供简洁的API。
* 提供一些业务上需要，但是标准库却没有提供的数据结构。

这个库除标准库外，不依赖其他任何东西，所以可以简单将其拷贝到 vendor/ 目录下，供业务使用。

因为我自己非常喜欢 Java，以及 Guava/Apache Commons 这样的库，所以这个库对他们有很深的模仿痕迹，：）

因为我将这个库视作自己的练习场，比如，我喜欢阅读 《Clean Code》，《重构》这样的书籍，然后会拿这个库来练手，练习如何设计让调用端感到好用的 API，
所以大概率上，这个库的 API 会不稳定。因此，大家应该按需拷贝自己所需要的代码。：）

这个库比较多的参考了Java和Go语言的某些习惯or特性，所以你大概率会从这些代码里面感受到它们的味道。：）

## Getting Started

### Installing
1. pip install py3utils

## Docs

### 常用的工具函数
为了减少调用者的记忆负担, 所有 Utils 都导入到 `py3uitls/__init__.py` 中, 所以可以这样使用:
```
# 调用者只需要关注这个命名空间, 后续不需要再导入其他任何东西( 这很像 Go 语言中的package 概念 )
import py3utils

py3utils.TimeUtils.get_current_timestamp()
```

这是为调用者提供的统一的命名空间, 则调用者完全不用关心实现代码位于哪个 py 文件中.

### 异常体系
异常 class 单独放在 `py3uitls.exceptions` 中, 按照如下形式导入:
```
import py3utils

try:

except py3utils.Py3UtilsException as e:

```

### 更多文档
请查看 docs/ (如果熟悉 Sphinx 工具, 则可以直接利用 Sphinx 构建出本地文档)

