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



# Example 
# $ python format.py  ./Invest/*.tsv
# --> will endup to Generated -folder

import sys 

def sanitize(stringMe):
	return stringMe.strip().lower()

def addHTMLmess(line):
	junk="\n\t<event"
	line=line.split("\t")
	junk = junk + "\n\t\tstart=\""+line[0].strip()+"\"\n "

	if sanitize(line[1]) != "na":
		junk = junk + "\t\tend=\""+line[1].strip()+"\"\n"

	if sanitize(line[2]) != "na":
		junk = junk + "\t\ttitle = \""+line[2].strip()+"\"\n\t\t"

	if sanitize(line[4]) != "na":
		junk = junk +"link=\""+line[4].strip()+"\"\n\t\t>\n"
	else:
		junk = junk +">\n"

	if sanitize(line[3]) != "na":
		junk = junk + "\t\t"+line[3].strip()
	
	junk = junk + "\n\t</event>"

	return junk


def main():
	 
	for f in sys.argv[1:]:
		print(str(f))
		data = open(str(f))
		line = data.readline()
		out = "<data>\n"

		while line != '':
			out = out + addHTMLmess(line)
			line = data.readline()
		
		data.close()
		newFile = open(str(f).split("/")[-1]+".xml", "w")
		newFile.write(out+"\n</data>")
		newFile.close()

#	 print(out+"\n</data>")
	

main()
