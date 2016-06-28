__author__ = 'hzchenzhe1'
import os
import sys
#current dir
curdir = os.getcwd()
keywords = ['SELECT','DELETE','UPDATE','INSERT','CREATE','WHERE','GROUP BY','ORDER BY']
print 'current dir: ' + curdir

if sys.argv[0]:
    curdir = sys.argv[0]
    print 'current dir change to: ' + curdir

#读取所有的xml 文件

#遍历xml文件list

#格式化操作
#读取文件内容，行
#逻辑： 目前只只对缩进和换行，记录碰到SELECT DELETE UPDATE INSERT CREATE，WHERE, GROUP BY ORDER BY,  都在行首开始缩进（n*4个tab), 每行只有一个以上关键字
#将文件内容写回

#end
