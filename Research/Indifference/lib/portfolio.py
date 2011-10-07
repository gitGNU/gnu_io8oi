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

"""
The purpose of this file is to create necessary functions
for MPT -portfolios.
"""




def portfolioReturn(props, profit):
   """ 
   Returns portfolio return.
   Requires proportions- and profit/returns -lists.
   """
   return sum([float(x)*float(y) for x, y in zip(props, profit)])


def portfolioStdDev(weights, correlation, stdDev):
   """
   Given the standard deviations of individual assets, 
   the function calculates the portfolio SD with the 
   different weights.
   """
   variance=0

   for i in range(len(weights)):
      for j in range(len(weights)):
         variance = variance + weights[i]*weights[j]*stdDev[i]*stdDev[j]*correlation[i][j]

   return (abs(variance))**(0.5)


def getProps(amountOfFunds):
   """
   Calculates random proportions for differen allocations.
   """
   props=[]

   # TODO: this part should be verified, uniform dist is a bit naive 
   # try other like exponential dist, random.random()

   for i in range(amountOfFunds):
      props = props + [random.uniform(0,1-sum(props))]

   random.shuffle(props)

   return props



