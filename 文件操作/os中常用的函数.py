#该模块通常与操作系统有关，即有些函数运行在Windows与MacOS中不一样
import os
import json
print(os.getcwd())#获取当前工作路径
lst=os.listdir()#列出当前路径下的所有目录文件
print(lst)
#创建目录,若存在则报错
# os.mkdir('test')
#删除目录,若不存在则报错
# os.rmdir('./test')
#删除多级目录,一起删除
# os.removedirs('./test/test1/test2')
#改变当前工作路径，但Python文件位置没有改变。
# os.chdir('../')
# print(os.getcwd())
#遍历目录树,递归操作
# for dirs,dirlst,filelst in os.walk(os.getcwd()):
#     print(dirs,dirlst,filelst)
#     print('---------------------------------')

#删除文件
# os.remove('./test.txt')
#重命名
#os.rename('./test.txt','./test1.txt')

#启动路径下的程序
# os.startfile('./test.exe')


