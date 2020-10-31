'''
Developed by Mu

This code can manually control the color used in python code

2020-10-29
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.cm as cm


def dcmap(file_path):
      fid=open(file_path)
      data=fid.readlines()
      n=len(data);
      rgb=np.zeros((n,3))
      for i in np.arange(n):
            rgb[i][0]=data[i].split(',')[0]
            rgb[i][1]=data[i].split(',')[1]
            rgb[i][2]=data[i].split(',')[2]
            rgb[i]=rgb[i]/255.0           
            icmap=mpl.colors.ListedColormap(rgb,name='my_color')                  
      return icmap



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
#map.pcolormesh(lons,lats,alb1,cmap=cmap)
map.pcolormesh(lons,lats,ek8,cmap=cmap)
#map.fillcontinents(color = 'white')
cb = map.colorbar(location = 'right')
cb.set_label('W*m^(-2)',fontsize = 15)
#cb.set_ticks(np.linspace(0,1350,11))
#cb.set_ticks(np.linspace(0,606,7))
cb.set_ticks(np.linspace(0,635,6))

#cb.set_ticklabels( ('0', '100', '200', '300', '400',  '500',  '600',  '700',  '800',  '900',  '1000',  '1100',  '1200',  '1300',  '1360'))
#cb.set_ticklabels( ('0', '135', '270', '405', '540',  '675',  '810',  '945',  '1080',  '1215',  '1350'))
#cb.set_ticklabels( ('0', '101', '202', '303', '404',  '505',  '606'))
cb.set_ticklabels( ('0', '127', '254', '381', '508',  '635'))

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
plt.title('SFC Upwelling Shortwave Flux(Clear-Sky)_SBDART',size=16)
#plt.savefig('h://sfc_albedo.png')
plt.show()
