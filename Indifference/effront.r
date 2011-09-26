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

#require('performanceAnalytics')  	# >R 2.9

require('RUnit')

.setUp()				# rUnits
YEAR=253 				# not 365 market days

calculateReturns <- function(files)
{
 profit=c()

 for (i in 1:length(files)){
  zz<-read.table(files[i], sep=';', header=FALSE)[[2]]

# profit = c( profit,  prod(1+diff(log(zz)))^(YEAR/length(zz)) - 1 )
  profit = c( profit,  prod(1+diff(zz) / zz[1:length(zz)-1] )^(YEAR/length(zz)) - 1 )
 }
 profit
}

calculateSds <- function(files)
{
 sds=c()

 for (i in 1:length(files)){
  zz<-read.table(files[i], sep=';', header=FALSE)[[2]]
  sdNew <- prod(1+tapply(zz, (seq_along(zz)-1) %/%YEAR, sd))^(YEAR/length(zz))
  sds = c(sds, sdNew-1 )
 }
 sds
}

createReturnStd<- function(files, name)
{
 jpeg(name)
 Risk = calculateSds(files)
 Return = calculateReturns(files)

 names <- strsplit(formatLabelTitles(files[1:length(files)]), ',')
 names <- unlist(names)

 dd<-data.frame(x=Risk, y=Return, name=names) #files[1:length(files)]) 
 plot(y~x, data=dd, xlab="Risk[Standard Deviation]", ylab="Return p.a.", main="Historical Risk Profile", xlim=c(0,4), ylim=c(-0.1,0.13))

 text(dd$x, dd$y, dd$name, pos=4)
 devNull <- dev.off()
}


timewiseStds<- function(file)
{
 zz <-read.table(file, sep=";", header=FALSE)[[2]]
 tapply(zz, (seq_along(zz)-1) %/%YEAR, sd)
}

maksValue <- function(files)
{
 maksValue<--1
 for (i in 1:length(files))
 {
  testValue <- length(timewiseStds(files[i]))

  if(maksValue < testValue)
  {
   maksValue <- testValue
  }
 }
 maksValue
}

createMatrix <- function(files, type)
{
#populating with NA values to the right size
 maks <- maksValue(files)
 m <-  seq(maks) %*%  t(seq(length(files)))
 m[,] <- NA

 for (i in 1:length(files))
 {
  #choosing right information
  if (type == 'SD') { populating <- timewiseStds(files[i]) } 
  if (type == 'R') { populating <- NA }

  years <- ceiling(nrow(read.table(files[i], header=FALSE))/YEAR)
  checkEquals(length(populating), years, 'Right amount of SDs calcutaled.')

  for (j in 1:years)
  {
# TODO NA values should be REMOVED from initial length measuring
   print(populating)
   print(str(populating))
   print(class(populating))
   off <- maks - length(populating)
   m[j+off,i] <- populating[j]
  }
 }
 m
}

formatLabelTitles <- function(labels)
{
 # trivial string formatting
 labels <- sub('./[^/]*/[^/]*/','',labels)
 labels <- sub('.csv$','',labels)
 labels <- sub('\n',',',labels)
 labels <- paste(unlist(labels), collapse=", ")

 labels
}


createHistoricalRiskCurves <-function(funds, name)
{
 m <- createMatrix(funds, 'SD')
 jpeg(name)
 funds <- formatLabelTitles(funds)

 matplot(m, main= strwrap(funds, width=50), ylab="Risk[StdDev]")
 matlines(m)
 devNull <- dev.off()
}

createEfficientFrontier <- function(files)
{
# SDs, Rs, Correlations
# THIS IS DONE IN PYTHON 
# itertools -pkg easier to use there
}

createCorrelationMatrix <-function(files)
{

  m <- zz<-read.table(files[1], sep=';', header=FALSE)[[2]]

 for (i in 2:length(files)){
  zz<-read.table(files[i], sep=';', header=FALSE)[[2]]
  m <- cbind(m,zz)
 }
 cor(m)
}


# FUNDS
active = paste("./Data/Active/", list.files(path="./Data/Active", pattern=".csv"), sep="")
passive = paste("./Data/Passive/", list.files(path="./Data/Passive", pattern=".csv"), sep="")

#print("Funds")
#print(passive)
#print("Return")
#calculateReturns(passive)
#print("Risk")
#calculateSds(passive)
#

# GRAPHS
createHistoricalRiskCurves(active, c('./Pictures/historicalActiveStdDev.jpeg'))
createHistoricalRiskCurves(passive, c('./Pictures/historicalPassiveStdDev.jpeg'))
createReturnStd(active, c('./Pictures/active_return_std.jpeg'))
createReturnStd(passive, c('./Pictures/passive_return_std.jpeg'))

