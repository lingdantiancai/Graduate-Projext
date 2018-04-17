# coding: utf-8
from termcolor import *

filename = input('Please input the file name:')

file = open('%s.txt'%(filename),'w')

file.write('folder:\n')

#ei = input('Please input the ei value:')#设置初试电压值
eh = input('Please input the eh value:')#设置高电压值
el = input('Please input the el value:')#设置低电压值
m  = float(input('Please input the simple mass:'))

#sens = 1e-1 #灵敏度
#print('\nThe sens value is default as: \'1e-1\'')#
#*************cv的数据*****************#
file.write('\nTech=cv')
file.write('\nei=%s'%(el))
file.write('\neh=%s'%(eh))
file.write('\nel=%s'%(el))
file.write('\nsens=0.1')


for i in range(3):
	file.write('\n\nv=0.1')
	file.write('\ncl=10')
	file.write('\nsens=0.1')
	file.write('\nrun')
	file.write('\nsave:cv100-%s'%(i))

file.write('\n\nTech=imp')
file.write('\nei=*******')
file.write('\nf1=0.01')
file.write('\nfh=100000')
file.write('\nrun')
file.write('\nsave:EIS')

cycleRate=[0.005,0.01,0.02,0.03,0.05,0.08,0.1,0.2,0.3,0.4,0.5]

file.write('\n\nTech=cv')
file.write('\nei=%s'%(el))
file.write('\neh=%s'%(eh))
file.write('\nel=%s'%(el))
file.write('\nsens=0.1')
file.write('\ncl=6')

for i in cycleRate:
	file.write('\n\nv=%s'%(i))
	file.write('\ncl=6')
	file.write('\nsens=0.1')
	file.write('\nrun')
	file.write('\nsave:cv%s'%(int(i*1000)))


#*************cp的数据*****************#
#cl = 5  cv曲线需要测试六段


file.write('\n\n\nTech=cp')
file.write('\neh=%s'%(eh))
file.write('\nel=%s'%(el))
file.write('\npn=n')
file.write('\nsi=0.01')
file.write('\ncl=7')



#file.write('\nsave:cp05')

value = m * 0.8   #计算样品中碳材料的质量
CurrenDensity = [1,2,3,5,8,10,15,20,30,40,50,60,80,100,0.5]#电流密度所用的倍率

for i in CurrenDensity:#不同电流密度下的测试参数
	if i == 0.5:		#判断如果下一个为0.5，那么调整参数为cl=7 si=0.01
		file.write('\nTech=cp')
		file.write('\neh=%s'%(eh))
		file.write('\nel=%s'%(el))
		file.write('\npn=n')
		file.write('\nsi=0.01')
		file.write('\ncl=7')

	file.write('\n\nic=%.6f'%(i*value))
	file.write('\nia=%.6f'%(i*value))
	file.write('\nrun')
	if i == 0.5:
		i = '005'
	file.write('\nsave:cp%s\n'%(i))
	if i == 5:
		file.write('\nTech=cp')
		file.write('\neh=%s'%(eh))
		file.write('\nel=%s'%(el))
		file.write('\npn=n')
		file.write('\nsi=0.001')
		file.write('\ncl=5')


file.close()#关闭文件


print('\nPlease add the  file path ') 
print(colored('\nThe auto program has been established, Plese check in thie folder','yellow'))
print(colored('\n\n\n\n\n\nPlease feel free to contact wiht me for any question about this program && email:lingdantiancai@163.com','red'))

while input() == 'd':
	brea










