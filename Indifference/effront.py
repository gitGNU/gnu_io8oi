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
global profit, stdDev, correlation


# Trial data with 9 funds
profit = [-0.088266066,0.047009708,0.043414530,0.004540003,0.050931110,-0.001456826,-0.016134395,0.028973769,0.078241841]
stdDev= [0.38311691,0.22665028,0.04058581,0.13716755,0.15418343,0.51986878,0.57533526,0.01715818,0.35563930]

correlation = [ [1.00000000,-0.4880688,-0.5655882,-0.02634336,-0.5546275,0.7273309,0.15655579,-0.6420619,-0.41715355], [-0.48806883,1.0000000,0.3113515,0.21199166,0.3956585,-0.5038957,0.25688729,0.2980148,0.39350958], [-0.56558822,0.3113515,1.0000000,-0.38622783,0.2304497,-0.3281015,-0.19737335,0.9834173,0.42190502], [-0.02634336,0.2119917,-0.3862278,1.00000000,0.7349999,0.1187878,-0.04373994,-0.3165645,0.58390567], [-0.55462755,0.3956585,0.2304497,0.73499986,1.0000000,-0.2401925,-0.14978985,0.3305895,0.80927157], [0.72733090,-0.5038957,-0.3281015,0.11878785,-0.2401925,1.0000000,-0.14467499,-0.3609108,-0.12097181], [0.15655579,0.2568873,-0.1973733,-0.04373994,-0.1497898,-0.1446750,1.00000000,-0.1843235,-0.05311217], [-0.64206187,0.2980148,0.9834173,-0.31656450,0.3305895,-0.3609108,-0.18432350,1.0000000,0.47845942], [-0.41715355,0.3935096,0.4219050,0.58390567,0.8092716,-0.1209718,-0.05311217,0.4784594,1.00000000] ] 

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
   trials = 1e5

   for time in range(trials):
      props=[]

# TODO: this part should be verified, uniform dist is a bit naive
# try other like exponential dist, random.random()

      for i in range(9):
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
   plotGraph(choice)
   saveImage()
 
main()
