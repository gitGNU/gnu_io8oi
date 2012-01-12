# Copyright (c) 2012, MathHarbour.com, Henri Losoi
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
#
# Description: 	creates QR codes on commandline with String -input,
#		optional size and optional msg. If no msg is given,
#		the msg will be the filename given.
#	
# Trial 0
# $ python bin/createQr.py -f verySimpleQr
#
# TRIAL 1
# $ python bin/createQr.py -f advancedQr -m 'I am 10801, yes!' -s 200



import qrencode 
import Image
import optparse


QR_ECLEVEL_L = 0
QR_ECLEVEL_M = 1
QR_ECLEVEL_Q = 2
QR_ECLEVEL_H = 3
levels = [QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_Q, QR_ECLEVEL_H]


QR_MODE_8 = 2
QR_MODE_KANJI = 3
hints = [QR_MODE_8, QR_MODE_KANJI]


def parseCli():
	parser = optparse.OptionParser()
	parser.add_option("-m", "--msg", dest="msg",
		     help="Message in QR code such as BC -hash and some string.", metavar="MSG")
	parser.add_option("-f", "--file", dest="filename",
		     help="Filename for the image.", metavar="FILE")
	parser.add_option("-s", "--size", dest="size",
		     help="Dimension of images, like 128, to generate.", metavar="SIZE")

	#TODO: create variety of sized QR codes for artistic things to T&E
	# parser.add_option("-n", "--number", dest="number",
		     #help="Number of images to generate", metavar="NUMBER")
	parser.add_option("-q", "--quiet",
		     action="store_false", dest="verbose", default=True,
		     help="Don't print status messages to stdout.")

	return parser.parse_args()

def main():

	def getMsg(myMsg, myFile):
		# returns the Msg for the image
		# msg is the filename if no msg otherwise msg
		if(myMsg):
			data=myMsg
		else:
			data=myFile
		return data

	(options, args) = parseCli()

	if (options.size and options.filename):
		# creates a file with user-defined size
		data=getMsg(options.msg, options.filename)
		size = int(options.size)	# must be before myFilename
		myFilename = './Pictures/'+options.filename+str(size)+'.gif'

		im=qrencode.encode_scaled(data, size, version=0, 
			level=QR_ECLEVEL_L, hint=QR_MODE_8,
		   	case_sensitive=True)[2]
		im.save(myFilename, "GIF")
		print('Created file: '+myFilename)

	elif (options.filename):
		# creates a very small picture by default without size
		data=getMsg(options.msg, options.filename)
		myFilename='./Pictures/'+options.filename+'.gif'

		im=qrencode.encode(data, version=0, 
			level=QR_ECLEVEL_L, hint=QR_MODE_8,
			case_sensitive=True)[2]
		im.save(myFilename, "GIF")
		print('Created file: '+myFilename)


main()



# REFERENCES
# QR functions: encode and encode_scaled [1]
#
# [1] https://github.com/Arachnid/pyqrencode/blob/master/qrencode/__init__.py
