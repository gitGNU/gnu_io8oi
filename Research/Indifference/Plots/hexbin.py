#!/usr/bin/env python
#
# Copyright (c) 2011, MathHarbour.com, Henri Losoi
# 
# Permission to use, copy, modify, and/or distribute this software
# for any purpose with or without fee is hereby granted, provided
# that the above copyright notice and this permission notice appear
# in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# 


"""
Goal is to find simpler ways to find pareto -points without actually
going them through. Only looking at some samples or general view.

1. Trial: frequency+normal Dist Ws (about right, needs C -matrix?)
2. Trial: Linear normalization with small-samples
3. Trial: cross-connected samle -normalization
4. Trial: large -sample normalization (bruteforce?)
"""


import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import random
import math



def attachTitles(data, titleTime):
	"""
	Attach titles to the hexbin -plot.
	Data means (SD, RETURN).
	"""

	x=np.array([float(t[1]) for t in data])

	#TODO: getting here negative numbes!??!
	y=np.array([float(t[0]) for t in data]) #[math.log(float(t[0])) for t in data])

	xmin = x.min()
	xmax = x.max()
	ymin = y.min()
	ymax = y.max()+0.1

	#plt.subplot(122)
	plt.hexbin(x,y,bins='log', cmap=cm.jet)
	plt.axis([xmin, xmax, ymin, ymax])
	plt.title("Crash Efficient Frontier")#, %s\n " 
	#	"hot colour for randomly-allocated portfolios."%(str(titleTime)))
	plt.xlabel("Portfolio return")
	plt.ylabel("Portfolio risk [ln(SD)]")
	cb = plt.colorbar()
	cb.set_label('log10(N) where N is occurencys')

	return plt


def attachLabels(labels, plt, data):
	"""
	Attach labels to the hexbin plot,
	data must have the form (SD, Return).
	"""

	#TODO: getting here negative numbes!??!
	y=np.array([float(t[0]) for t in data]) #[math.log(float(t[0])) for t in data])
	ymax = y.max()+0.1


	rets = data[1]
	sds = data[0]

	## ATTACH THE LABELS TO THE HEXPLOT
	#
	for (i,rrr,sss,lll) in zip(range(len(rets)), rets, sds, labels):
		plt.annotate(
			lll,
			xy=(rrr,sss),

			# Hashing function to get the dots to the middle
			xytext=(rrr-0.03, (ymax-sss)/3+i/10),
			arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
		)

	return plt


# TODO: replace the data retrieval with readVals -function
#
# EXAMPLE
#
# Individual fund data 
#labels= [ 1, 2 , 3 , 4, ..., 999]
#
#
# READING PORTFOLIO COMBINATION points
# READ tuple(SD, return) FROM FILES SDs and RETURNS
#f = file(".data", "r").readlines()
#combs = [x.rstrip().split("\t") for x in f]
#rets = [float(r) for r in file("RETURNS", "r").readlines()]
#sds = [float(s) for s in file("SDs", "r").readlines()]
#dataas=np.array([[float(x),float(y)] for (x,y) in zip(rets,sds)])
#
#
#
#data = # (SD, Return)
#plt = attachTitles(data, titleTime):
#plt = attachLabels(labels, plt, data)
#
#plt.show()
