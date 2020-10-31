'''
Developed by Mu

transform era5data to SBDART usable kind
contain geopotential,o3 mass mixing ratio,specific humidy,temperature

2020-10-18
'''

import xarray as xr
import numpy as np
     
data = xr.open_dataset('h://ERA5NEW.nc')
#transform data to sbdart readable type,n is lat;m is lon
'''
z = (data['z']).mean(dim=('time'))   #geopotential m**2/s**2
o3 = (data['o3']).mean(dim=('time'))  #o3 mass mixing ratio kg/kg
q = (data['q']).mean(dim=('time'))   #specific humidy kg/kg
t = (data['t']).mean(dim=('time'))   #temperature K
p = data['level']
'''  
z = data['z']  #geopotential m**2/s**2
o3 = data['o3'] #o3 mass mixing ratio kg/kg
q = data['q']  #specific humidy kg/kg
t = data['t']  #temperature K
p = data['level']
z = z[0,:,:]
o3 = o3[0,:,:]
q = q[0,:,:]
t = t[0,:,:]

z = z/(9.8*1000)
wd = 217*q*p/(0.622*t)
od = (o3*(p/(287.05/t)))
    
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


def trans(n,m):
    a = np.zeros((38,5))
    for i in range(0,37):
        a[i,0] = z1[i,n,m]
        a[i,1] = p[i]
        a[i,2] = t1[i,n,m]
        a[i,3] = q1[i,n,m]
        a[i,4] = o31[i,n,m]
    
    #np.savetxt('i:\\atms.dat',a,fmt='%f,%f,%f,%f,%f')
    f = open('f:/sbdart_atms_cld/atms_' + str(n) +'_'+ str(m) + '.dat','w')
    f.write('37')
    
    for i in range(0,37):
        f = open('f:/sbdart_atms_cld/atms_' + str(n) +'_'+ str(m) + '.dat','a')
        f.write('\n'+str(a[i,0])+' '+str(a[i,1])+' '+str(a[i,2])+' '+str(a[i,3])+' '+str(a[i,4])) 
        f.close()	


for i in range(0,180):
    for j in range(0,360):
        trans(i,j)


        