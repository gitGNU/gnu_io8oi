import lib.effront as ef
import lib.readDateVals as rv
import glob
import math
import numpy

#print rv.aves([1,2,8,1,4])

# Data
files = sorted(glob.glob("./TestDATA/.*.csv"))
datas = rv.readDatas(files)
arr = rv.dateWiseValsList(datas)
arr = rv.rmPlaceholders(arr, 0)

# Valuations
# some annualized, correlation is not
sds = rv.sds(arr, 365)
res = rv.returns(arr, 365)
correlMatrix =  numpy.corrcoef(arr)

print "SDs are \n", sds
print "Returns are \n", res
print "Correlations are \n", correlMatrix

