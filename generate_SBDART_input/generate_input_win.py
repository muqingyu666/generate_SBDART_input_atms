'''
Developed by Mu

transform modis,snpp,era5data to SBDART usable kind
contain albedo,sun zenith angle,cloud water path,cloud effective radius,cloud top height

2020-10-17
'''

import xarray as xr
import netCDF4 as nc
import numpy as np
import copy

with nc.Dataset('h://modis_cld.nc') as f:
            cloud_water_path_liquid = f.groups["Cloud_Water_Path_Liquid"]   
            lwp = cloud_water_path_liquid.variables["Mean"][:,:]
            cld_top_pressure = f.groups["Cloud_Top_Pressure"]   
            cld_p = cld_top_pressure.variables["Mean"][:,:]      

with nc.Dataset('h://snpp_cld.nc') as f:
            cloud_effective_radius = f.groups["Cloud_Effective_Radius_Liquid"] #获取group的ID
            nre = cloud_effective_radius.variables["Mean"][:,:] #获取group/组中的变量
            cloud_top_height = f.groups["Cloud_Top_Height"] #获取group的ID
            cth = cloud_top_height.variables["Mean"][:,:] #获取group/组中的变量

data = xr.open_dataset('h://albedo.nc')
#transform data to sbdart readable type,n is lat;m is lon
alb = (data['fal']).mean(dim=('time'))   #geopotential m**2/s**2
alb1 = np.zeros((180,360))
for j in range(0,360):
    for i in range(0,180):
            alb1[i,j]=np.mean(alb[4*i:4*(i+1),4*j:4*(j+1)])


a = xr.open_dataset('h://ceres.nc')
sza=a.solar_zen_angle_1hm
sza00=sza[0,:,:]

alb1 = np.flipud(alb1)
alb_1,alb_2=np.split(alb1,2,axis=1)
alb=np.c_[alb_2,alb_1]

sza_1,sza_2=np.split(sza00,2,axis=1)
sza00=np.c_[sza_2,sza_1]

sza00[sza00>89]=90

lwp = lwp.data
cth = cth.data
nre = nre.data
cth[cth<0]=0
cth = cth/1000

lwp[lwp < -100]=0
cth[cth < -100]=0
nre[nre < -100]=2
nre[nre < 2]=2
LWP=copy.copy(lwp)
LWP[np.where(nre ==2)]=0
CTH=copy.copy(cth)
CTH[np.where(nre ==2)]=0

LWP=np.transpose([LWP])
CTH=np.transpose([CTH])
nre=np.transpose([nre])
LWP=LWP[:,:,0]
CTH=CTH[:,:,0]
nre=nre[:,:,0]

text=('\n'+' &INPUT '+'\n'
      "  wlinf=0.25"+'\n'
      "  wlsup=4"+'\n'
      "  wlinc=0.005"+'\n'
      "  idatm=0"+'\n'
      "  isalb=0"+'\n'
      "  iout=10"+'\n'
      )


def write(n,m):
    #f = open('h:/sbdart_input/INPUT_' + str(n) +'_'+ str(m) ,'w')
    f = open('f://sbdart_input_cld/INPUT' + str(n) +'_'+ str(m)  ,'w')
    f.write(text)
        
    f = open('f://sbdart_input_cld/INPUT' + str(n) +'_'+ str(m)  ,'a')
    f.write('  lwp='+str(LWP[n,m])+'\n'
          '  sza='+str(sza00[n,m])+'\n'
          '  zcloud='+str(CTH[n,m])+'\n'
          '  albcon='+str(alb[n,m])+'\n'
          '  nre='+str(nre[n,m])+'\n'
    	    "/") 
    f.close()	


for i in range(0,179+1):
      for j in range(0,359+1):
            write(i,j)

