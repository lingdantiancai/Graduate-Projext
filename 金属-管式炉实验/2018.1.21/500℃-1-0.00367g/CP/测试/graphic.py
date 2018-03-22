import matplotlib.pyplot as plt
import numpy as np 
import os


#获取文件，剔除掉没用的字符，将数据缓存在新建文本里面进行操作
def getValue(filename):
	cache = open('cache.txt','w')

	with open(filename,'r') as f:
		#value = f.read()
		x=0
		for i in f.readlines():
			x = x + 1
			if x >= 20:
				#print (i)
				cache.write(i)
	cache.close()

def findpoint(y):		#设定一个函数来寻找图像中第二个最小点
	p = [] 		#建立一个数组，存储最小点的位置
	for i in range(len(y)):
		if i>2 and i<len(y)-2:
			if y[i]<y[i-1] and y[i]<y[i+1]:		#找出比两边点都小的点位置并且输出
				 p.append(i)
	return p 			 
				
def drawing(xlabel,ylabel,title,label):#传入x轴标签，y轴标签，以及坐标轴名称
	
	x,y = np.loadtxt('cache.txt', delimiter=',', unpack=True) #读取文件，以逗号为界点，开始画图	
	p = findpoint(y)		#从findpoint函数中获取最小点位置列表
	
	plt.plot(x[p[1]:],y[p[1]:],label=filename[:4],linewidth = 1,color='black') #以找到的第二个最小点为分界点画图；x[p[1]:]表示最小点以后的数据
	plt.xlabel(xlabel)  
	plt.ylabel(ylabel)  
	plt.title(title)  
	plt.legend()  
	plt.show()
	os.remove('cache.txt')






#filename = 'CP15.txt'
#getValue('CP15.txt')
#drawing('Time/sec','Potential/V',filename[:4],filename[:4])












