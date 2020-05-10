'''
Created on 2020年4月10日

@author: 船长
'''
"""
import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
from sys import path,argv
print('================Python import mode==========================')
print ('命令行参数为:')
for item in argv:
    print (item);
print ('\n python 路径为',path);