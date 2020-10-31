

import netCDF4 as nc


with nc.Dataset('h://modis_cld.nc') as f:
            cloud_water_path_liquid = f.groups["Cloud_Water_Path_Liquid"]   
            lwp = cloud_water_path_liquid.variables["Mean"][:,:]
            cld_top_pressure = f.groups["Cloud_Top_Pressure"]   
            cld_p = cld_top_pressure.variables["Mean"][:,:]      

with nc.Dataset('h://snpp_cld.nc') as f:
            cloud_effective_radius = f.groups["Cloud_Effective_Radius_Liquid"] #获取group的ID
            nre = cloud_effective_radius.variables["Mean"][:,:] #获取group/组中的变量

lwp = lwp.data
cld_p = cld_p.data
nre = nre.data

lwp[lwp<-100]=0
cld_p[cld_p<-100]=0
nre[nre<-100]=0

cld_h = 44300*(1-(cld_p/1013.25)**(1/5.256))

text=('\n'+' &INPUT'+'\n'
      "  IDATM=4          , AMIX= -1.0000000000000000     , ISAT=0          , WLINF= 0.25     , WLSUP= 4     , WLINC=  0.005     ,"+'\n'
      "  SZA=  0.0000000000000000     , CSZA= -1.0000000000000000     , SOLFAC=  1.0000000000000000     , NF=2          ,"+'\n'
      "  IDAY=0          , TIME=  16.000000000000000     , ALAT= -64.766998291015625     , ALON= -64.067001342773438     , ZPRES= -1.0000000000000000     ,"+'\n'
      "  PBAR= -1.0000000000000000     , SCLH2O= -1.0000000000000000     , UW= -1.0000000000000000     , UO3= -1.0000000000000000     , O3TRP= -1.0000000000000000     ,"+'\n'
      "  ZTRP=  0.0000000000000000     , XRSC=  1.0000000000000000     , XN2= -1.0000000000000000     , XO2= -1.0000000000000000     , XCO2= -1.0000000000000000     ,"+'\n'
      "  XCH4= -1.0000000000000000     , XN2O= -1.0000000000000000     , XCO= -1.0000000000000000     , XNO2= -1.0000000000000000     , XSO2= -1.0000000000000000     ,"+'\n'
      "  XNH3= -1.0000000000000000     , XNO= -1.0000000000000000     , XHNO3= -1.0000000000000000     , XO4=  1.0000000000000000     , ISALB=0          ,"+'\n'
      "  ALBCON=  0.0000000000000000     , SC= 0  , TCLOUD= 0.0000000000000000       , RHCLD= -1.0000000000000000     , KRHCLR=0          , JAER= 0          ,"+'\n'
      "  ZAER= 0.0000000000000000       , TAERST= 0.0000000000000000       , IAER=0          , VIS= -1.0000000000000000     , RHAER= -1.0000000000000000     , TBAER= -1.0000000000000000     ,"+'\n'
      "  WLBAER= -1.0000000000000000      , QBAER= -1.0000000000000000      , ABAER=  0.0000000000000000     , WBAER= -1.0000000000000000      , GBAER= -1.0000000000000000      ,"+'\n'
      "  PMAER= -1.0000000000000000      , ZBAER= -1.0000000000000000      , DBAER= -1.0000000000000000      , NOTHRM=-1         , NOSCT=0          , KDIST=3          ,"+'\n'
      "  ZGRID1=  1.0000000000000000     , ZGRID2=  30.000000000000000     , NGRID=0          , IDB= 0          , ZOUT=  0.0000000000000000     ,  100.00000000000000     ,"+'\n'
      "  IOUT=10         , PRNT= F, TEMIS=  0.0000000000000000     , NSTR=0          , NZEN=0          , UZEN= -1.0000000000000000      , VZEN= 90.000000000000000       ,"+'\n'
      "  NPHI=0          , PHI= -1.0000000000000000      , SAZA=  180.00000000000000     , IMOMC=3          , IMOMA=3          , TTEMP= -1.0000000000000000     ,"+'\n'
      "  BTEMP= -1.0000000000000000     , CORINT=F, SPOWDER=F, ")

#f = open('h:/sbdart_input/INPUT_' + str(n) +'_'+ str(m) ,'w')
f = open('h:/sbdart_input/INPUT' ,'w')
f.write(text)
    

f = open('h:/sbdart_input/INPUT' ,'a')
f.write('\n'+'  '+'LWP='+str(lwp[i,0])+'             , '+'ZCLOUD='+str(cld_h[i,1])+'             , '+'NRE='+str(nre[i,2])+'             , '+'\n'
	   "   /") 
f.close()	
