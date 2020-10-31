import xarray as xr
import numpy as np
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"]=proj_lib
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.cm as cm

     
data = xr.open_dataset('/home/muqy20/era5data.nc')
#transform data to sbdart readable type,n is lat;m is lon
z = (data['z']).mean(dim=('time'))   #geopotential m**2/s**2
o3 = (data['o3']).mean(dim=('time'))  #o3 mass mixing ratio kg/kg
q = (data['q']).mean(dim=('time'))   #specific humidy kg/kg
t = (data['t']).mean(dim=('time'))   #temperature K
p = data['level']
    
z = z/(9.8*1000)
wd = 217*q*p/(0.622*t)
od = (o3*(p/(287.05/t)))

#decrease the spactral resolution of ERA5 data    
z1 = np.zeros((37,180,360))
q1 = np.zeros((37,180,360))
t1 = np.zeros((37,180,360))
o31 = np.zeros((37,180,360))
for i in range(0,180):
    for j in range(0,360):
        for x in range(0,37):
            z1[x,i,j]=z[x,4*i,4*j]
            q1[x,i,j]=wd[x,4*i,4*j]
            t1[x,i,j]=t[x,4*i,4*j]
            o31[x,i,j]=od[x,4*i,4*j]


#cut the data into -180,180 type
for i in range(0,37):
    o31[i,:,:] = np.flipud(o31[i,:,:])
    z1[i,:,:] = np.flipud(z1[i,:,:])
    t1[i,:,:] = np.flipud(t1[i,:,:])
    q1[i,:,:] = np.flipud(q1[i,:,:])


o3_1,o3_2=np.split(o31,2,axis=2)
o3=np.c_[o3_2,o3_1]

z_1,z_2=np.split(z1,2,axis=2)
z=np.c_[z_2,z_1]

t_1,t_2=np.split(t1,2,axis=2)
t=np.c_[t_2,t_1]

q_1,q_2=np.split(q1,2,axis=2)
q=np.c_[q_2,q_1]



'''
for i in range(0,180):
    for j in range(0,360):
        for x in range(0,37):
            z1[x,i,j]=z[x,4*i,4*j]
            q1[x,i,j]=wd[x,4*i,4*j]
            t1[x,i,j]=t[x,4*i,4*j]
            o31[x,i,j]=od[x,4*i,4*j]
'''

def trans2(n,m):
    a = np.zeros((38,5))
    for i in range(0,37):
        a[i,0] = z[i,n,m]
        a[i,1] = p[i]
        a[i,2] = t[i,n,m]
        a[i,3] = q[i,n,m]
        a[i,4] = o3[i,n,m]
    
    #np.savetxt('i:\\atms.dat',a,fmt='%f,%f,%f,%f,%f')
    f = open('/home/muqy20/sbdart_atms1/atms_' + str(n) +'_'+ str(m) + '.dat','w')
    f.write('37')
    
    for i in range(0,37):
        f = open('/home/muqy20/sbdart_atms1/atms_' + str(n) +'_'+ str(m) + '.dat','a')
        f.write('\n'+str(a[i,0])+' '+str(a[i,1])+' '+str(a[i,2])+' '+str(a[i,3])+' '+str(a[i,4])) 
        f.close()   


for i in range(0,180):
    for j in range(0,360):
        trans2(i,j)

