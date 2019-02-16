'''
l 查看代码
n 执行一行
b 增加断点
clear 删除断点
p 查看参数
a 查看所有
r 到最后一行

'''
import pdb

def average(a,b):
	return (a+b)/2


a=100
b=200
pdb.set_trace()
c=average(a,b)
print(c)