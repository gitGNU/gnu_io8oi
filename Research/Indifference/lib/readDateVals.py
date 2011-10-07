from collections import defaultdict
import math
import itertools
import glob
import numpy
import sys
import datetime as dt
from datetime import datetime as dtt

"""
Creating data-structures for the data dat is in CSV files.
Works only with FULL data, no null values allowed or empty
slots. So each timeserie must be of the same lenght.
Otherwise, the statistical signifinance may change!

The data is daily valuations for different time-series,
like stock-valuations for many corps.
"""

#files = sorted(glob.glob(".*.csv"))
#datas = [[ c.split(";") for c in file(f, "r")]
#			for f in files]

#TODO: 
# Rewrite R SDs for python, found in effront.r
# 1. calculateSds <- function(files)
# 2. calculateReturns <- function(files)
# 3. itertools.ifilter(predicate, iterable) to process list?


def readDatas(files):
	"""
	Return the content of the files assumping that
	the date and valuation separated by ";".

	It also checks that your files are of the right
	format i.e. of the same size.
	"""

	contents = [[ c.split(";") for c in file(f, "r")]
				for f in files]

	lenghts = [len(c) for c in contents]
	
	if sum([l%lenghts[0] for l in lenghts]) != 0:
		sys.exit("Sorry each file must be of the same size.")
	

	return [[ c.split(";") for c in file(f, "r")]
				for f in files]

def readFiles(pathRegex):
	"""
	Gets you the files.
	For example, try ".*.csv"
	"""

	return sorted(glob.glob(pathRegex))


def oldestNewestDates(datas):
	"""
	datas contain data of each file with (date, val) -list
	if you have CSV files, simple use:

	files = sorted(glob.glob("*.csv"))
	datas = [[ c.split(";") for c in file(f, "r")] for f in files]
	"""
	try:
		oldestDate = min([dtt.strptime(d[0][0], '%d.%m.%Y') for d in datas])
		newestDate = max([dtt.strptime(d[-1][0], '%d.%m.%Y') for d in datas])
	except ValueError:
		print "Your datas is \n", datas
		sys.exit("It is probably empty.")
		
	
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


def dateWiseValsDict(datas2):
	# UNORDERED...not easy to get samples...
	d = defaultdict(list)
	for i,j in itertools.chain.from_iterable(datas2):
	     d[i].append(float(j))
	
	return d


def sds(dataMatrix, period):
	"""
	Use dateWiseValsList(datas) to get the dataMatrix.
	Retuns normalized Sds period, variance divided by 
	days in the period.

	Period is a number over which to calculate the sds,
	like 365 for annualized. (Better read effront.r.)
	
	OBS! Sample normalization
	numpy.cov calculates sample covariance i.e. 
	division by (N-1) not by N where N is sample size.
	"""
	#TODO: results unexpectedly high....
	return [(numpy.cov(row)/len(row)*period)**0.5 for row in dataMatrix]


def returns(dataMatrix, period):
	"""
	Use dateWiseValsList(datas) to get the dataMatrix.
	Calculate returns

	OBS! Ave is wholeHistory -ave, not period ave.
	"""
	aves = [numpy.average(row) for row in dataMatrix]

	try:
		dailyReturns = [[(math.log(obs)-math.log(ave))/period 
					for obs in row]
					for row, ave in zip(dataMatrix,aves)]

		returns = [numpy.average(rets) for rets in dailyReturns]
	except ValueError:
		print "Either you have negative valuations or"
		sys.exit("CSV -files are not of the same lenght.")

	return returns


def correls(dataMatrix, period):
	"""
	Use dateWiseValsList(datas) to get the dataMatrix.
	
	OBS! Hsitorical correlations, not periodical,
	which can change quite a bit due to economically 
	significant periods. During downturn, more finance etc.
	"""

	return numpy.corrcoef(dataMatrix)


def aves(dataMatrix):
	"""
	Use dateWiseValsList(datas) to get the dataMatrix.
	Returns averages for time-series.
	"""
	return [numpy.average(row) for row in dataMatrix]



# EXAMPLES
#
# Data
#arr = dateWiseValsList(datas)
#arr = rmPlaceholders(arr, 0)
#
## Valuations
## some annualized, correlation is not
#sds = sds(arr, 365)
#res = returns(arr, 365)
#correlMatrix =  numpy.corrcoef(arr)
#
#
#print "SDs are \n", sds
#print "Returns are \n", res
#print "Correlations are \n", correlMatrix
