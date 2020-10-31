import xlrd
import xarray as xr
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#从EXCEL文件中读取数据并进行处理
def excel(n):
    wb = xlrd.open_workbook('H:\\output1.xlsx')# 打开Excel文件
    sheet1_content1 = wb.sheet_by_name('Sheet1')#通过excel表格名称(rank)获取工作表
    cols = sheet1_content1.col_values(n)
    return cols


t = excel(1) #返回整个函数的值
t = np.array(t)
t = t.reshape((180,360))


lon = np.linspace(100,105,21)
lat = np.linspace(75,80,21)

fig = plt.figure(figsize=(10, 10))
plt.rc('font', size=10, weight='bold')
ax = fig.add_subplot(111)
#basemap设置部分
map = Basemap(projection='cyl',llcrnrlat=75,urcrnrlat=80,llcrnrlon=100,urcrnrlon=105,resolution='l')
map.drawcountries(linewidth=1.5)
map.drawcoastlines()
map.drawparallels(np.linspace(100,105,21),labels=[1,0,0,0],fontsize=15)
map.drawmeridians(np.linspace(75,80,21),labels=[0,0,0,1],fontsize=15)
map.drawlsmask()
lons, lats = np.meshgrid(lon, lat)
cmap=dcmap('D:\\colormap\\test.txt')
map.pcolormesh(lons,lats,t,cmap=cmap)
map.colorbar(location = 'right')
#map.colorbar.set_label('Flux(W/m2)',fontdict=font)

#设置横纵坐标
lon_num = np.arange(100, 105, 0.75)
print(lon_num)
lon_label = ['100' ,'100.75', '101.5', '102.25' ,'103','103.75','104.5']
lat_num = np.arange(75, 80, 0.75)
print(lat_num)
lat_label = ['75', '75.75', '76.5' ,'77.25', '78' ,'78.75', '79.5' ]
plt.yticks(lat_num, lat_label)
plt.xticks(lon_num, lon_label)

plt.title('Upward Shortwave Flux at Top of Atmosphere',size=20)
#plt.savefig('Flux1.png')
plt.show()
