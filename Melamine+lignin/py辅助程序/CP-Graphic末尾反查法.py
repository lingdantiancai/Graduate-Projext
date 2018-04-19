# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np 
import os



i = 0	#搭配选择颜色的参数
colors = ['red','aqua','black','blue','brown','cyan','darkred','firebrick','green','ivory','magenta','brown','darkgoldenrod','darkslategray','blanchedalmond','dimgray','khaki','lightcoral']#这是一个颜色库，后面画图会使用
#获取文件，剔除掉没用的字符，将数据缓存在新建文本里面进行操作
path = 'C:/Users/lingd/Google Drive/毕业设计/毕业设计/实验数据/Graduate-Projext/Melamine+lignin/20180413/1000-碱性/CP'
#path = 'C:/Users/lingd/Google Drive/毕业设计/毕业设计/实验数据/Graduate-Projext/Melamine+lignin/py辅助程序'
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
	i = int(len(y))
	sign = False
	for a in range(i):
		v = y[i-a-1]-y[i-a-8]#减去当前位置之前值，来判断增减性。其中8的设置是为了避免近距离数值之间的波动造成误差
		
		if v<=0: 
			if sign == False:
				continue
			elif sign == True:
				print(i-a,y[i-a-1])
				return i-a
				break
		if v>0:
			sign = True
			
			

	


def drawing(xlabel,ylabel,title,label):#获取该文件中需要进行绘图的点

	x,y = np.loadtxt('cache.txt', delimiter=',', unpack=True) #读取文件，以逗号为界点，获取参数点	
	p = findpoint(y)		#获取最小点位置
	
	print (p,y[p-2],y[p-1],y[p])#判断当前寻找的值前后数值是否大于最小值
	#plt.plot(x[p-1:]-x[p-1],y[p-1:],label=filename[:4],linewidth = 1,color='black') #以找到的第二个最小点为分界点画图；x[p[1]:]表示最小点以后的数据
	
	return x[p-1:],y[p-1:]
	
	os.remove('cache.txt')#操作处理完成后 删除缓存文件

#os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list


#建立一个独立的文件夹，将处理后的数据放在这里面
folder = os.path.exists('%s/Precessed-data'%(path))  
if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹  
    os.makedirs('%s/Precessed-data'%(path))            #makedirs 创建文件时如果路径不存在会创建这个路径  
    print ("---Processed data has been save in Precessed-data ---")
    print ("---  OK  ---")




for file in os.listdir(path):

    if file[-3: ] == 'txt' and file[:5] != 'cache':

    	file = ''.join(file.split())
    	print(file)
    	getValue(file)
    	x,y=drawing('Time/sec','Potential/V',file,file)
    	#print(x[1]) 获取每一个图像的起始时间值，并将其置0

    	x = x-x[0]
    	#将处理后的数据重新建立一个文本存储

   # 	Temp = open('Precessed-data/%s-Processed.txt'%(file[:-4]),'w')#将处理后数据存储于当前程序文件夹
    	Temp = open('%s/Precessed-data/%s-Processed.txt'%(path,file[:-4]),'w')#将处理后数据存储在目标文件夹
    	Temp.write('%s\n'%(file))
    	for u in range(len(x)):
    		Temp.write('%s,%s \n'%(x[u],y[u]))
    	Temp.close()


    	plt.plot(x,y,label=file,linewidth = 1,color=colors[i])
    		
    else:
    	continue
    i = i+1



plt.xlabel('Time/sec')  #设置x，y轴标签，标题等
plt.ylabel('Potential/V')
plt.title('CPgraphic')  
plt.legend()
plt.show()
os.remove('cache.txt')	















