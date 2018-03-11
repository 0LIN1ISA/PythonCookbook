# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/11 11:51

"""
第10章 模块与包
"""

"""
10.1 模块与包
"""
# 只要在每个目录中定义一个__init__.py文件，使其封装成包

# graphics/formats/__init__.py
# from . import jpg
# from . import png
# __init__.py会自动加载子模块

"""
10.2 控制模块被全部导入的内容
"""


# 使用 from module import * ,会从模块或者包全部导入
# 如果想精确控制导入哪些包，可以定义变量__all__来控制
# somemodule.py
def spam():
    pass


def grok():
    pass


blah = 42
# only export 'spam' and 'grok'
__all__ = ['spam', 'grok']

"""
10.3 使用相对路径名导入包中的子模块
"""
# from . import grok
# from ..B import spam

"""
10.4 将模块分割成多个文件
"""
# 将文件分割成多个文件，组织在一个目录mymodule下，然后在__init__.py中导入
# from . import A
# from . import B
# import mymodule
# a = mymodule.A
# a.span()
# b = mymodule.B
# b.grok()

"""
10.5 利用命名空间导入目录分散的代码
"""
import sys

sys.path.extend(['foo-package', 'bar-package'])
# foo-package和bar-package都有相同的命名空间spam，且同时没有__init__.py文件
# import spam.blah
# import spam.grok

"""
10.6 重新加载模块
"""
# 使用imp.reload()来重新加载先前加载过的模块
# import spam
import imp

imp.reload()

"""
10.7 运行目录或压缩文件
"""
# zai 顶层目录下存放文件__main__.py即可

# python myapp.zip

"""
10.8 读取位于包中的数据文件
"""
import pkgutil,data

data = pkgutil.get_data('data', 'somedata.dat')
print(data)

"""
10.9 将文件夹加入到sys.path
"""
# 第一种：使用PYTHONPATH环境变量
# bash % env PYTHONPATH=/some/dir:/other/dir python3

# 第二种：在python中添加
import sys
sys.path.append('3:\\python36')

# 第三种：在Python的site-packages目录中，创建.pth文件
# myapp.pth
# /some/dir
# /other/dir

"""
10.10 将字符串名导入模块(动态导入模块，无法自动补全函数、类等)
"""
import importlib
my_math = importlib.import_module('math')
print(my_math.sin(2))

"""
10.11 通过导入钩子远程加载模块
"""

"""
10.12 导入模块的同时修改模块
"""

"""
10.13 安装私有的包
"""

"""
10.14 创建新的Python环境
"""

"""
10.15 分发包
"""