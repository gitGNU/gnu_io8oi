import urllib
import xlrd
from pylab import *



url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
fXls = 'ie_data.xls'
urllib.urlretrieve(url, fXls)

wb = xlrd.open_workbook(fXls)
sh = wb.sheet_by_name(u'Data')


p=sh.col_values(7)[8:-10]
d=sh.col_values(8)[8:-10]
e=sh.col_values(9)[8:-10]

y = [(ee+dd)/pp for ee,dd,pp in zip(e,d,p)]
x=sh.col_values(10)[8:-10]

plot(x[128:-1], y[128:-1])

title('Historical Return versus PE10, based on Schiller Data')
show()
