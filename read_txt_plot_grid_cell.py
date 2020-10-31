from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.cm as cm

filename = 'f://output_cld.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
ek1 = []
ek2 = []
ek3 = []
ek4 = []
ek5 = []
ek6 = []
ek7 = []
ek8 = []
ek9 = []
with open(filename, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
      break
      pass
    e1, e2, e3, e4, e5, e6, e7, e8, e9 = [float(0) if i =='NaN' else float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
    ek4.append(e4)
    ek5.append(e5)  # 添加新读取的数据
    ek6.append(e6)
    ek7.append(e7)
    ek8.append(e8)
    pass
  ek4 = np.array(ek4) 
  ek5 = np.array(ek5) # 将数据从list类型转换为array类型。
  ek6 = np.array(ek6)
  ek7 = np.array(ek7)
  ek8 = np.array(ek8)
  pass


for i in range(0,231):
              ek4 = np.delete(ek4,62871-i)
              ek5 = np.delete(ek5,62871-i)
              ek6 = np.delete(ek6,62871-i)
              ek7 = np.delete(ek7,62871-i)
              ek8 = np.delete(ek8,62871-i)
              
          
ek5.shape
ek8.shape
ek5 = ek5.reshape((180,360))
#ek5 = np.reshape((150,360))
ek8 = ek8.reshape((180,360))
ek4 = ek4.reshape((180,360))
ek7 = ek7.reshape((180,360))

netswbot=ek7-ek8
netswtop=ek4-ek5
ek8[ek8>12.3]=0
ek5 = np.array(ek5)
ek5[ek5<60]=0
ek5 = ek5.reshape((180,360))
ek7 = ek7.reshape((180,360))
ek8 = ek8.reshape((180,360))
ek4=[0 if i =='NaN' else i for i in ek4]
#t = map(eval, t)

lon = np.linspace(-180,180,360)
lat = np.linspace(-90,90,180)

fig = plt.figure(figsize=(10, 10))
plt.rc('font', size=10, weight='bold')
ax = fig.add_subplot(111)
#basemap设置部分
map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='l')

parallels = np.arange(-90,90+30,30) #纬线
map.drawparallels(parallels,labels=[True,False,False,False],linewidth=0.01,dashes=[1,400])
plt.yticks(parallels,len(parallels)*[''])
meridians = np.arange(-180,180+30,30) #经线
map.drawmeridians(meridians,labels=[False,False,False,True],linewidth=0.01,dashes=[1,400])
plt.xticks(meridians,len(meridians)*[''])

#map.drawcountries(linewidth=1.5)
map.drawcoastlines()
#map.drawparallels(np.linspace(0,360,360),labels=[1,0,0,0],fontsize=15)
#map.drawmeridians(np.linspace(-90,90,180),labels=[0,0,0,1],fontsize=15)
map.drawlsmask()
lons, lats = np.meshgrid(lon, lat)
cmap=dcmap('F://color/test.txt')
cmap.set_under('gray')
map.pcolormesh(lons,lats,ek7,cmap=cmap)
#map.pcolormesh(lons,lats,netswbot,cmap=cmap,vmax=542.6,vmin=460)
#map.fillcontinents(color = 'white')
cb = map.colorbar(location = 'right')
cb.set_label('W*m^(-2)',fontsize = 15)
#map.colorbar.set_label('Flux(W/m2)',fontdict=font)
'''
#设置横纵坐标
lon_num = np.arange(-180, 180, 25)
#lon_label = ['100' ,'100.75', '101.5', '102.25' ,'103','103.75','104.5']
lat_num = np.arange(-90, 90, 25)
#lat_label = ['75', '75.75', '76.5' ,'77.25', '78' ,'78.75', '79.5' ]
plt.yticks(lat_num)
plt.xticks(lon_num)
'''
plt.title('SFC Downwelling Shortwave Flux(Clear-Sky)_SBDART',size=16)
#plt.savefig('Flux1.png')
plt.show()
