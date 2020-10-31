import numpy as np
import matplotlib.pyplot as plt
import xlrd

def excel(n):
    wb = xlrd.open_workbook('E:\\exe.xlsx')# 打开Excel文件
    sheet1_content1 = wb.sheet_by_name('Sheet1')#通过excel表格名称(rank)获取工作表
    cols = sheet1_content1.col_values(n)
    return cols

wave = excel(0) #返回整个函数的值
up = excel(2)
dn = excel(3)

wave = np.array(wave)
up = np.array(up)
dn = np.array(dn)

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1 = ax.plot(wave, up, color='blue',label='upward SW spectral irradiance')
#line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
# Using plot(..., dashes=...) to set the dashing when creating a line
line2 = ax.plot(wave, dn, color='red',label='downward SW spectral irradiance')
ax.set_xlabel('wavelength(um)',fontsize=15)
ax.set_ylabel('W/m2/um',fontsize=15)
ax.legend()
plt.title('Upwelling and Downwelling SW Spectral Irradiance',fontsize=15)
plt.show()
