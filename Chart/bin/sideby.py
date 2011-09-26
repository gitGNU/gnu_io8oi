# Description: plots historical PE10 graphs to avoid euphoria
# License: OpenBSD license
# Author: 10801


import urllib
import xlrd
from pylab import *

plot([1,2,3])

url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
fXls = 'ie_data.xls'
urllib.urlretrieve(url, fXls)

wb = xlrd.open_workbook(fXls)
sh = wb.sheet_by_name(u'Data')

x=sh.col_values(0)
y=sh.col_values(10)

subplot(211)
plot(x[128:-1], y[128:-1])
title('Graphs are based on R. Shiller data \n\n Historical PE10 versus Time')


#2nd plot 
p=sh.col_values(7)[8:-10]
d=sh.col_values(8)[8:-10]
e=sh.col_values(9)[8:-10]

y = [(ee+dd)/pp for ee,dd,pp in zip(e,d,p)]
x=sh.col_values(10)[8:-10]

subplot(212)
plot(x[128:-1], y[128:-1])
title('Real Return versus PE10')


show()

