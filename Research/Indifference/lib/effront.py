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

import itertools, os, operator, random
import glob
import plotting, portfolio

"""
The purpose of this file is to generate different Efficient Frontiers
i.e. graphs vizualising returns and standard deviations.
"""

def createEffronts(choice):
	"""
	Generates different types of effronts.
	1. hexplot (better to scatter plot with density)
	2. crash frontier or drawdown -plot with worst case scenario
	3. bull frontier -plot with best case scenario
	4. average frontier -plot with average case scenario
	5. ALLOW different Pareto -situations?
	"""



#def main():
#   #1 efficient frontier
#   #2 just points
#
#   amountOfFunds = 13
#
#   weights = getProps(amountOfFunds)
#   correlation = 
#   stdDev = 
#   returns = 
#
#   choice = 1
#   density = 1e6
#
#   points = generatePoints(choice, returns, density)
#
#   portSd = portfolioStdDev(props)
#   portRe = portfolioReturn(props, returns)
#
#   saveResults(points)
#   saveImage()
#   plotGraph(choice)
#   saveImage()
# 
#main()
