from collections import defaultdict
import itertools
import glob
import numpy
import datetime as dt
from datetime import datetime as dtt

"""
Creating data-structures for the data dat is in CSV files

The data is daily valuations for different time-series,
like stock-valuations for many corps.
"""

files = sorted(glob.glob(".*.csv"))
datas = [[ c.split(";") for c in file(f, "r")]
			for f in files]

def oldestNewestDates(datas):
	"""
	datas contain data of each file with (date, val) -list
	if you have CSV files, simple use:

	files = sorted(glob.glob("*.csv"))
	datas = [[ c.split(";") for c in file(f, "r")] for f in files]
	"""

	oldestDate = min([dtt.strptime(d[0][0], '%d.%m.%Y') for d in datas])
	newestDate = max([dtt.strptime(d[-1][0], '%d.%m.%Y') for d in datas])
	
	return oldestDate, newestDate


def nextDay(dateTimeDate):
	"""
	datetime.date(2002, 12, 30)
	"""
	return dateTimeDate + dt.timedelta(days=1)

def lastDay(dateTimeDate):
	"""
	datetime.date(2002, 12, 30)
	"""
	return dateTimeDate - dt.timedelta(days=1)

def isWeekend(dateTimeDate):
	#Sunday = 6, Saturday = 5
	#http://docs.python.org/library/datetime.html
	
	if dateTimeDate.weekday() == 5:
		#print "The type is ", type(dateTimeDate)
		#print "It is saturday", dateTimeDate
		return True
	elif dateTimeDate.weekday() == 6:
		#print "The type is ", type(dateTimeDate)
		#print "It is sunday", dateTimeDate
		return True
	else:
		return False


#if you have a list, sort it by the timestampts and use itertools.ifilter

def dateWiseValsList(datas):
	"""
	Create a list data-structure the same to dateWiseValsDict
	but in List
	"""

	oldestDate, newestDate = oldestNewestDates(datas)
	days = (newestDate - oldestDate).days
	result = [[0]*len(datas) for a in xrange((days+1))]

	# Index: day - oldestDate, oldestDate = 0
	# TODO: check THAT DATA GETS TO RIGHT PLACE, pUnit

	for date, val in itertools.chain.from_iterable(datas):

		# Empty slots for NA with this indexing...
		dateComp = dtt.strptime(date, '%d.%m.%Y')
		ind = (dateComp - oldestDate).days

		# 1st ~ day, 2nd ~ Insert to the first occurred-NA the value
		result[ind][result[ind].index(0)] = float(val)

	return result
	

def rmPlaceholders(myList, placeholder):
	"""
	Removes placeholder lines such as 0 and NAs
	"""
	return numpy.array([numlist for numlist in myList if numlist[0] is not placeholder])

#def dateWiseValsDict(datas2):
#	# UNORDERED...not easy to get samples...
#	d = defaultdict(list)
#	for i,j in itertools.chain.from_iterable(datas2):
#	     d[i].append(float(j))
#	
#	return d
#

#def readLists(lists):
	#itertools.ifilter(predicate, iterable)
	


#TODO: rewrite this R SDs for python
#
#calculateSds <- function(files)
#{
# sds=c()
#
# for (i in 1:length(files)){
#  zz<-read.table(files[i], sep=';', header=FALSE)[[2]]
#  sdNew <- prod(1+tapply(zz, (seq_along(zz)-1) %/%YEAR, sd))^(YEAR/length(zz))
#  sds = c(sds, sdNew-1 )
# }
# sds
#}

#TODO: rewrite this R Returns for python
#
#calculateReturns <- function(files)
#{
# profit=c()
#
# for (i in 1:length(files)){
#  zz<-read.table(files[i], sep=';', header=FALSE)[[2]]
#
## profit = c( profit,  prod(1+diff(log(zz)))^(YEAR/length(zz)) - 1 )
#  profit = c( profit,  prod(1+diff(zz) / zz[1:length(zz)-1] )^(YEAR/length(zz)) - 1 )
# }
# profit
#}




#CORRELATION matrix
arr =  dateWiseValsList(datas)
arr = rmPlaceholders(arr, 0)




print arr
#print numpy.corrcoef(arr)
#print numpy.std(arr)
