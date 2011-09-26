import urllib
import xlrd
from pylab import *



url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
fXls = 'ie_data.xls'
urllib.urlretrieve(url, fXls)

wb = xlrd.open_workbook(fXls)
sh = wb.sheet_by_name(u'Data')

x=sh.col_values(0)
y=sh.col_values(10)

plot(x[128:-1], y[128:-1])

title('Historical PE10, based on Schiller Data')
show()
