#range函数
#返回值是一个range类的对象，该对象是可迭代对象（意思就是包含返回迭代器对象的iter方法）
# range(stop) 从0到stop  range(start,stop) 从start到stop，左闭右开 range(start,stop,step)从start到stop，步长为step
k = range(5).__iter__()
# print(k.__next__())
#range负步长场景，确保start小于end(大于end也不会报错，只是没有满足条件的数，返回结果为空)，就可以向后计数了
#print(list(range(1,2,-2)))

range(0, 5)[2:4]#todo看不懂这个什么玩意

#python的docstring,这样的注解可以在help命令时被显示，python内置的对象都是可以通过help方式查看说明的
class MyDocumentClass:
    '''this class is well documented but doesn't do anything special.'''
    def do_nothing():
        '''method documented'''
        pass
# help(list)
#python pass关键字 python将缩进用于代码块的方式，使得需要代码块的地方是不可以留空的,会有语法错误，此时可以补充一个pass
#pass的主要用途1）用于创建断点，比如在函数体末尾设置断点，就可以在末尾添加一个pass
#pass在开发阶段可以多次使用，比如某个方法的实现留着后续完成或者辅助调试，但一般生产代码带pass是没有意义的
#留一个0或者空字符串等都是可以实现相同效果的，但使用pass是标准，用来表示这里是故意留空的
def do_something():
    pass

#python与操作系统的交互
#python读写文件,使用with statement确保文件关闭，read一次性读入文件所有内容，文件较大时不适合这样处理
# with open('C:/Users/王宏/notepad/python.txt','r',encoding='utf-8') as f: #不指定encoding时，默认是使用操作系统默认的编码方式，可能与读取的文件编码不一致
#     print(f.read())

#将文件按行一次性读入list中，list(f)和调用f的readlines方法两种方式
# with open('C:/Users/王宏/notepad/python.txt',encoding='utf-8') as f:
#     # list1 = list(f)
#     list2 = f.readlines()
#     print(list2[1])

#逐行读取文件，将打开的文件视为迭代器(看起来python将一些本来应该自行定义的功能给找了个追加实践默认，比如迭代文件内容就没有将所有内容读入内存后再迭代)
# with open('C:/Users/王宏/notepad/python.txt','r',encoding='utf-8') as f:
#     for line in f:
#         print(line)

#python中删除文件，创建目录，移动文件等操作大多都在os模块中，需要导入os模块使用
#os.path的isdir和isfile检测目录或文件是否存在
import http.client
import http.server
import os
# os.mkdir('mydir')#不指定路径，默认的是python项目路径
#os.mkdir('C:/Users/王宏/notepad/mydir')#绝对路径创建目录，结尾的/写不写都行，不能递归创建，不能覆盖创建，及要求上级目录存在，要求要创建的目录不存在

#os的移动功能只限于同个文件系统，如果要实现linux上的mv功能（就算不在同个文件系统上也可以移动），可以使用shutil的功能
import shutil
# shutil.move('C:/Users/王宏/notepad/mydir','C:/Users/王宏/notepad/mydir1')#可以用移动实现改名的目的

import subprocess
# subprocess.run(['python --version'])

#python虚拟环境，第三方包的管理工具，可以轻松安装特定于项目和环境的软件包，使用requirements.txt为所需包定义确切的版本号
#通过venv将项目依赖隔离，相比于本地依赖，修改一个依赖的版本可能会影响其他项目
#就是有几个python的包管理工具，通过该工具下载包时，对应的依赖包也会自动下载，依赖包的版本都写在配置文件中方便查阅


#python并发，python本身只支持单线程（同时只有一个线程在运行，就是说多核心没什么用），也可以通过第三方库启用多线程（实际上是启动了多个python进程实现的）
#cpu密集型的程序，多线程是没多少用处的，主要是io密接型的程序，可以使用多线程（同时也只有一个线程在运行，线程在io时可以让其他线程运行）



