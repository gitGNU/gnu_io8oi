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

import os

"""
The purpose of this file is to provide necessary plotting solutions
for indifferent situations. One of such situation is the pareto
optimality with efficient frontiers and also the decision making
problem for which vizualization is prerequisite.
"""


#PLOTTING FUNCTIONS!!!??!

def plotGraph(choice):
   #TODO: replace this with the Python option in Chart -dir

   if (int(choice) == 1):
      os.system("gnuplot -e \"set title 'Efficient Frontier'; set ylabel 'Return'; set xlabel 'Risk [Standard devitation]'; plot '.data' with lines; pause -1;\"")
   if (int(choice) == 2):
      os.system("gnuplot -e 'set grid; splot \".data\"; pause -1'")

def saveImage():
   os.system("gnuplot -e \"set terminal png; set output './Pictures/effront.png'; plot '.data'\"")


def saveResults(points):
   f = open('.data', 'w')
   f.write(points)
   f.close()


