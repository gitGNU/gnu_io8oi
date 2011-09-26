import urllib
import xlrd
from matplotlib import pyplot
from pylab import *
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random

#DOWNLOADING DATA
url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
fXls = 'ie_data.xls'
urllib.urlretrieve(url, fXls)

wb = xlrd.open_workbook(fXls)
sh = wb.sheet_by_name(u'Data')

#XYZ -coordinates
p=sh.col_values(7)[8:-10]
d=sh.col_values(8)[8:-10]
e=sh.col_values(9)[8:-10]

y=[(ee+dd)/pp for ee,dd,pp in zip(e,d,p)]
x=sh.col_values(10)[8:-10]
#title('Real return and PE10, based on Schiller Data')
subplot(211)
plot(x,y)

z=sh.col_values(0)[8:-10]
x=sh.col_values(10)[8:-10]
#title('Time and PE10, based on Schiller Data')
subplot(212)
plot(x,z)

show()

