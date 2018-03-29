# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np 
import os

i = 0	#搭配选择颜色的参数
colors = ['red','aqua','black','blue','brown','cyan','darkred','firebrick','green','ivory']#这是一个颜色库，后面画图会使用
#获取文件，剔除掉没用的字符，将数据缓存在新建文本里面进行操作
path = 'C:/Users/lingd/Google Drive/考研复试&毕业设计/毕业设计/毕业设计/实验数据/Graduate-Projext/Melamine+lignin/2018.3.22--2\CP\drawing'

def getValue(filename):
	cache = open('cache.txt','w')
	file = '%s/%s'%(path,filename)
	print(file)
	with open(file,'r') as f:
		#value = f.read()
		x=0
		for i in f.readlines():
			x = x + 1
			if x >= 21:
				#print (i)
				cache.write(i)
	cache.close()
'''
def findpoint(y):		#设定一个函数来寻找图像中第二个最小点
	p = [] 		#建立一个数组，存储最小点的位置
	for i in range(len(y)):
		if i>1 and i<len(y)-1:
			if y[i]<y[i-1] and y[i]<y[i+1]:		#找出比两边点都小的点位置并且输出
				 p.append(i)
	return p 			 
'''		
def findpoint(y):#另外一种寻找中值最小点的方式
	i = int(len(y)/2)#直接切入数据的中间，然后查看该数据旁边两个数据的大小。
	a = i
	print (i,y[i])#然后向数据缩小的方向寻找最小值
	if y[i]<y[i+1] and y[i]<y[i-1]:
		return i


	elif y[i]<=y[i+1]:
		while (y[i]<=y[i+1]):
			i = i - 1
		if y[i]>y[i+1]:
			pass
		else:
			return i
	elif y[a]<=y[a-1]:
		while (y[a]<=y[a-1]):
			a = a + 1
		if y[a]>y[a-1]:
			pass
		else:
			return a


def drawing(xlabel,ylabel,title,label):#获取该文件中需要进行绘图的点

	x,y = np.loadtxt('cache.txt', delimiter=',', unpack=True) #读取文件，以逗号为界点，获取参数点	
	p = findpoint(y)		#从findpoint函数中获取最小点位置列表
	
	print (p,y[p-2],y[p-1],y[p])
	#plt.plot(x[p[1]:],y[p[1]:],label=filename[:4],linewidth = 1,color='black') #以找到的第二个最小点为分界点画图；x[p[1]:]表示最小点以后的数据
	
	return x[p-1:],y[p-1:]
	
	os.remove('cache.txt')#操作处理完成后 删除缓存文件

#os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
for file in os.listdir(path):

    if file[-3: ] == 'txt' and file[:5] != 'cache':

    	#filetype=os.path.splitext(file)[1]
    	#filename=os.path.splitext(file)[0] #获取文件原名
    	file = ''.join(file.split())
    	print(file)
    	getValue(file)
    	x,y=drawing('Time/sec','Potential/V',file,file)
    	#print(x[1]) 获取每一个图像的起始时间值，并将其置0
    	print(file)
    	plt.plot(x-x[0],y,label=file,linewidth = 1,color=colors[i])
    		
    else:
    	continue
    i = i+1



plt.xlabel('Time/sec')  #设置x，y轴标签，标题等
plt.ylabel('Potential/V')
plt.title('CPgraphic')  
plt.legend()
plt.show()
os.remove('cache.txt')	















