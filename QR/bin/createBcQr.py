

# TODO: reuse the createQR -function for this
# TODO: THE LAYOUT to separate file.
# TODO: SH -script
#
# Trial 0
# $ python bin/createQr.py -f verySimpleQr
#
# TRIAL 1
# $ python bin/createQr.py -f advancedQr -m 'I am 10801, yes!' -s 200

amount=0.5
imUrl='https://sites.google.com/site/mathharbour/search/qrCode_mh.gif'
label="MathHarbour.com"

print('Give me the BC code\n')
code=raw_input()

image='<div>\n<a href="bitcoin:'+code+'?amount='+str(amount)+'&label="'+label+'">\n <img src="'+imUrl+'" ></a> \n <p>'+code+'</p>\n </div>'

textQr='<img src="http://ansrv.com/png?s=http://blockexplorer.com/q/getreceivedbyaddress/'+code+'&amp;c=000000&amp;b=FFFFFF&amp;size=5" />'

print('\n'+image+'\n\n')

print(textQr)
