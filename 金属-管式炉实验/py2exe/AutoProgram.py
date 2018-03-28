# coding: utf-8
from termcolor import *
file = open('AutoProgramForCV.txt','w')

file.write('folder:\n')

#ei = input('Please input the ei value:')#设置初试电压值
eh = input('Please input the eh value:')#设置高电压值
el = input('Please input the el value:')#设置低电压值
m  = float(input('Please input the simple mass:'))

#sens = 1e-1 #灵敏度
#print('\nThe sens value is default as: \'1e-1\'')#

cl = 5  #cv曲线需要测试六段

file.write('\nTech=cp')
file.write('\neh=%s'%(eh))
file.write('\nel=%s'%(el))
file.write('\npn=n')
file.write('\nsi=0.01')
file.write('\nrun')#

#file.write('\nsave:cp05')

value = m * 0.8   #计算样品中碳材料的质量
CurrenDensity = [0.5,1,2,3,5,8,10,15,20,40,60]#电流密度所用的倍率

for i in CurrenDensity:#不同电流密度下的测试参数
	file.write('\n\nic=:%.6f'%(i*value))
	file.write('\nia=:%.6f'%(i*value))
	file.write('\nrun')
	file.write('\nsave:cp%s'%(i))
file.close()#关闭文件

print('\nThe number of Segments is default as: \'%s\''%(cl))
print('\nThe value of \'si\' is 0.1')
print('\nPlease add the  file path ') 
print(colored('\nThe auto program has been established, Plese check in thie folder','yellow'))
print(colored('\n\n\n\n\n\nPlease feel free to contact wiht me for any question about this program && email:lingdantiancai@163.com','red'))
while input() == 'd':
	break










