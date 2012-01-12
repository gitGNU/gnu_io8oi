import qrencode 
import Image
import StringIO

QR_ECLEVEL_L = 0
QR_ECLEVEL_M = 1
QR_ECLEVEL_Q = 2
QR_ECLEVEL_H = 3
levels = [QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_Q, QR_ECLEVEL_H]


QR_MODE_8 = 2
QR_MODE_KANJI = 3
hints = [QR_MODE_8, QR_MODE_KANJI]

print('I will create you an QR image.\n\n')
data=raw_input('Text =')

#TRIAL 1
#im=qrencode.encode(data, version=0, level=QR_ECLEVEL_L, hint=QR_MODE_8,
	   #case_sensitive=True)[2]
#im.save('./Pictures/tinyTiny.gif', "GIF")

#TRIAL 2
size = 100
im=qrencode.encode_scaled(data, size, version=0, level=QR_ECLEVEL_L, hint=QR_MODE_8,
	   case_sensitive=True)[2]
im.save('./Pictures/'+data+str(size)+'.gif', "GIF")

# REFERENCES
#
# QR functions: encode and encode_scaled
#https://github.com/Arachnid/pyqrencode/blob/master/qrencode/__init__.py
