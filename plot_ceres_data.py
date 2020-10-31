'''
Developed by Mu

plot data from ceres, compare to the model result

2020-10-24
'''

import xarray as xr
import numpy as np
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


def max(n):
      k=np.max(n)               
      return k


data = xr.open_dataset('h://ceres.nc')
toa_solar = data['toa_solar_all_1hm']
cl_sfc_up = data['ini_sfc_sw_up_clr_1hm']
al_toa_dn = data['ini_toa_sw_all_1hm']
al_sfc_up = data['ini_sfc_sw_up_all_1hm']
al_sfc_dn = data['ini_sfc_sw_down_all_1hm']

toa_solar1 = toa_solar[0,:,:]
cl_sfc_up1 = toa_sfc_up[0,:,:]
al_toa_dn1 = al_toa_dn[0,:,:]
al_sfc_up1 = al_sfc_up[0,:,:]
al_sfc_dn1 = al_sfc_dn[0,:,:]

toa_1,toa_2=np.split(toa_solar1,2,axis=1)
cl_solar1=np.c_[toa_2,toa_1]

toa1_1,toa1_2=np.split(cl_sfc_up1,2,axis=1)
cl_sfc_up1=np.c_[toa1_2,toa1_1]

toa2_1,toa2_2=np.split(al_toa_dn1,2,axis=1)
al_toa_dn1=np.c_[toa2_2,toa2_1]

toa3_1,toa3_2=np.split(al_sfc_up1,2,axis=1)
al_sfc_up1=np.c_[toa3_2,toa3_1]

toa4_1,toa4_2=np.split(al_sfc_dn1,2,axis=1)
al_sfc_dn1=np.c_[toa4_2,toa4_1]

#############################################################################

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
map.pcolormesh(lons,lats,al_sfc_dn1,cmap=cmap)
#map.fillcontinents(color = 'white')
cb = map.colorbar(location = 'right')
cb.set_label('W*m^(-2)',fontsize = 15)
#cb.set_ticks(np.linspace(0,1350,11))
#cb.set_ticks(np.linspace(0,606,7))
#cb.set_ticks(np.linspace(0,635,6))
#cb.set_ticks(np.linspace(0,595,6))
cb.set_ticks(np.linspace(0,950,6))
#cb.set_ticklabels( ('0', '100', '200', '300', '400',  '500',  '600',  '700',  '800',  '900',  '1000',  '1100',  '1200',  '1300',  '1360'))
#cb.set_ticklabels( ('0', '135', '270', '405', '540',  '675',  '810',  '945',  '1080',  '1215',  '1350'))
#cb.set_ticklabels( ('0', '101', '202', '303', '404',  '505',  '606'))
#cb.set_ticklabels( ('0', '127', '254', '381', '508',  '635'))
#cb.set_ticklabels( ('0', '116', '232', '348', '464',  '580'))
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
plt.title('SFC Downwelling Shortwave Flux(All-Sky)_CERES',size=16)
#plt.savefig('h://sfc_albedo.png')
plt.show()
