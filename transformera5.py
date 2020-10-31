'''
develope by MU
2020.8.19
'''

import xarray as xr
import numpy as np
     
def trans(n,m):
    data = xr.open_dataset('h://era5data.nc')
    #transform data to sbdart readable type,n is lat;m is lon
    z = (data['z']).mean(dim=('time'))   #geopotential m**2/s**2
    o3 = (data['o3']).mean(dim=('time'))  #o3 mass mixing ratio kg/kg
    q = (data['q']).mean(dim=('time'))   #specific humidy kg/kg
    t = (data['t']).mean(dim=('time'))   #temperature K
    p = data['level']
    
    z = z/(9.8*1000)
    wd = 217*q*p/(0.622*t)
    od = (o3*(p/(287.05/t)))
    
    a = np.zeros((38,5))
    for i in range(0,37):
        a[i,0] = z[i,n,m]
        a[i,1] = p[i]
        a[i,2] = t[i,n,m]
        a[i,3] = wd[i,n,m]
        a[i,4] = od[i,n,m]
    
    #np.savetxt('i:\\atms.dat',a,fmt='%f,%f,%f,%f,%f')
    f = open('h:/sbdart_atms/atms_' + str(n) +'_'+ str(m) + '.dat','w')
    f.write('37')
    
    for i in range(0,37):
        f = open('h:/sbdart_atms/atms_' + str(n) +'_'+ str(m) + '.dat','a')
        f.write('\n'+str(a[i,0])+' '+str(a[i,1])+' '+str(a[i,2])+' '+str(a[i,3])+' '+str(a[i,4])) 
        f.close()	
