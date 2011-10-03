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
# Example # $ python format.py -a DFA, Warren Buffett, William
# Bernstein, Benjamin Graham -f Invest/misc.tsv, Invest/people.tsv
# |less 

import sys


def sanitize(stringMe):
	return stringMe.strip().lower()

def parseCliPars():

	from optparse import OptionParser

	parser = OptionParser()
	parser.add_option("-f", "--files", dest="filenames",
			  action="store", type="string",
			  help="write files.tsv like 'file.tsv, file2.tsv'")
	parser.add_option("-q", "--quiet",
			  action="store_false", dest="verbose", default=True,
			  help="don't print status messages to stdout")
	parser.add_option("-a", "--authors", dest="authors",
			  action="store", type="string",
			  help="select authors")

	(options, args) = parser.parse_args()


	print options.authors

	return options.authors, options.filenames


def fileExist(fileTest):
	try:
		fTest=open(fileTest)
		fTest.close()
		return True
	except IOError:
		return False


def getQuotes(authors, fs):
	quotes=""

	for f in [y.strip() for y in fs.split(",")]:
		if not fileExist(f):
			sys.exit("Your given file %s does not exist."%str(f))
		ff = open(f)
		line = ff.readline()

		while line != "":
			author = sanitize(line.split("\t")[0])
			print author, authors, sanitize(author) in authors

			if author in authors:
				quotes = quotes + line
			line = ff.readline()
	return quotes


def main():
	authors, fs = parseCliPars()
	quotes =""
	authors = set([sanitize(x) for x in authors.split(",")])
	quotes = getQuotes(authors, fs)
	
	print quotes

main()


