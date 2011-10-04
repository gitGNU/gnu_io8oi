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
One vizualization block.
"""

import numpy as np
import pylab as P
import matplotlib.pyplot as plt


data = [x.rstrip().split("\t") for x in file(".data", "r").readlines()]
sdData = [float(x[1]) for x in data]
retData =[float(x[0]) for x in data]

# Calculating medians for estimating mean and sd
retMed = sorted(sdData)[len(sdData)/2]
sdMed= sorted(retData)[len(sdData)/2]

fig = plt.figure()
ax = fig.add_subplot(111)
#print retMed, sdMed


mu, sigma = retMed, sdMed
x = mu + sigma*P.randn(10000)

# the histogram of the data with histtype='step'
n, bins, patches = P.hist(x, 20, normed=1, histtype='stepfilled')
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

# add a line showing the expected distribution
y = P.normpdf( bins, mu, sigma)
l = P.plot(bins, y, 'k--', linewidth=1.5)


#
# create a histogram by providing the bin edges (unequally spaced)
#
ax.set_ylabel("Minus return, -r")
ax.set_xlabel("Normalized occurrences")
P.title("Random portfolio return over XYZ days\nMedian SD = XYZ%PA. Median Return = ZYX%PA")
P.figure()
P.show()
