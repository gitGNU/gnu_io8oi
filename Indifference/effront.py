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
global profit, stdDev, correlation

#one column per file to python-list
def getColumn(myFile):
	with open(myFile, 'r') as fd:
		return [float(x) for x in fd]

# Trial data with funds

profit = getColumn("RETURNS")
stdDev = getColumn("SDs")

cF = file("CORmatrix", "r").readlines()
files = sorted(glob.glob("*.csv"))


# TODO: corcoeff
# files are of different lenght, fill the empty spots with NA
#
# Use scipy to creat the correlation matrix (instead of R)
# http://www.scipy.org/Numpy_Example_List#column_stack
# http://www.scipy.org/Numpy_Example_List#head-779283aaa3cc20a3786ad33c2ee1fee9d68a4a53

def sparseCorrMatrix(fs):
	a = 0*len(fs)
	for i,f in enumerate(fs):
		with open(f, 'r') as c:
			a[i] = [float(x.split(';')[1]) for x in file(c, 'r')]
	for fc in a:
		# Handle here the sparse data
		# NA values must be in the beginning of the time -serie
		# Better make them correspond to the days, some indices
		# may not be open every day...
		

#TODO: replace this wit hspareCorrMatrix -function
correlation = [[ 1.000000, -0.729665, -0.932800,  0.934353,  0.746531,  0.890790,  0.978546,  0.937087,  0.923152,  0.938789, -0.781900,  0.936309,  0.8614123], [-0.729665,  1.000000,  0.805225, -0.890261, -0.241180, -0.614191, -0.802933, -0.893384, -0.901166, -0.663586,  0.925643, -0.692262, -0.9322848], [-0.932800,  0.805225,  1.000000, -0.950803, -0.591330, -0.808678, -0.949406, -0.925533, -0.931088, -0.849201,  0.856070, -0.949737, -0.8558980], [ 0.934353, -0.890261, -0.950803,  1.000000,  0.524278,  0.793792,  0.970159,  0.984997,  0.984762,  0.839748, -0.924360,  0.921980,  0.9515590], [ 0.746531, -0.241180, -0.591330,  0.524278,  1.000000,  0.847638,  0.662232,  0.556424,  0.505916,  0.845705, -0.226091,  0.633182,  0.4158362], [ 0.890790, -0.614191, -0.808678,  0.793792,  0.847638,  1.000000,  0.876986,  0.832558,  0.811880,  0.960749, -0.609994,  0.805363,  0.7615057], [ 0.978546, -0.802933, -0.949406,  0.970159,  0.662232,  0.876986,  1.000000,  0.975331,  0.971062,  0.924888, -0.864929,  0.941320,  0.9203610], [ 0.937087, -0.893384, -0.925533,  0.984997,  0.556424,  0.832558,  0.975331,  1.000000,  0.990586,  0.878594, -0.919218,  0.884496,  0.9759533], [ 0.923152, -0.901166, -0.931088,  0.984762,  0.505916,  0.811880,  0.971062,  0.990586,  1.000000,  0.858448, -0.947523,  0.890894,  0.9779451], [ 0.938789, -0.663586, -0.849201,  0.839748,  0.845705,  0.960749,  0.924888,  0.878594,  0.858448,  1.000000, -0.680508,  0.830558,  0.8087444], [-0.781900,  0.925643,  0.856070, -0.924360, -0.226091, -0.609994, -0.864929, -0.919218, -0.947523, -0.680508,  1.000000, -0.780268, -0.9516406], [ 0.936309, -0.692262, -0.949737,  0.921980,  0.633182,  0.805363,  0.941320,  0.884496,  0.890894,  0.830558, -0.780268,  1.000000,  0.7960807], [ 0.861412, -0.932284, -0.855898,  0.951559,  0.415836,  0.761505,  0.920361,  0.975953,  0.977945,  0.808744, -0.951640,  0.796080,  1.0000000]] 

def portfolioReturn(props, profits):
   """ needs proportions- and profit/returns -lists """
   return sum([float(x)*float(y) for x, y in zip(props, profits)])

def portfolioStdDev(values):
   variance=0

   for i in range(len(values)):
      for j in range(len(values)):
         variance = variance + values[i]*values[j]*stdDev[i]*stdDev[j]*correlation[i][j]

   return (abs(variance))**(0.5)

def plotGraph(choice):

   if (int(choice) == 1):
      os.system("gnuplot -e \"set title 'Efficient Frontier'; set ylabel 'Return'; set xlabel 'Risk [Standard devitation]'; plot '.data' with lines; pause -1;\"")
   if (int(choice) == 2):
      os.system("gnuplot -e 'set grid; splot \".data\"; pause -1'")


def generatePoints(choice):
   points=""
   trials = int(1e6)

   for time in range(trials):
      props=[]

# TODO: this part should be verified, uniform dist is a bit naive
# try other like exponential dist, random.random()

      for i in range(13):
         props = props + [random.uniform(0,1-sum(props))]
      random.shuffle(props)

      if (int(choice) == 1):
            portReturn = portfolioReturn(props, profit)
       	    points = points + "%s\t%s\n"%(str(portfolioStdDev(props)), str(portReturn))
      if (int(choice) == 2):
            points = points + "%s\n"%(str(props))

   return points

def saveImage():
   os.system("gnuplot -e \"set terminal png; set output './Pictures/effront.png'; plot '.data'\"")


def saveResults(points):
   f = open('.data', 'w')
   f.write(points)
   f.close()


def main():
   #1 efficient frontier
   #2 just points

   choice = 1
   points = generatePoints(choice)
   saveResults(points)
   saveImage()
   plotGraph(choice)
   saveImage()
 
main()
