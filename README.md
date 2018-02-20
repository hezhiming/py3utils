# py3utils: Useful Python 3 utils

Some useful Python 3 utils.

## Getting Started

### Installing
1. pip install py3utils

## Docs

### 常用的工具函数
为了减少调用者的记忆负担, 所有 Utils 都导入到 `py3uitls/__init__.py` 中, 所以可以这样使用:
```
from py3utils import (Url, OSUtils, DatetimeUtils)
```

这是为调用者提供的统一的命名空间, 则调用者完全不用关心实现代码位于哪个 py 文件中.

### 异常体系
异常 class 单独放在 `py3uitls.exceptions` 中, 按照如下形式导入:
```
from py3utils.exceptions import Py3UitlsException

try:

except Py3UtilsException as e:

```

### 更多文档
请查看 docs/ (如果熟悉 Sphinx 工具, 则可以直接利用 Sphinx 构建出本地文档)

