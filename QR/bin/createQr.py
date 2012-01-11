

print('Give me the BC code\n')
code=raw_input()
#print('Give me the QR image.') 

image='<div>\n <a href="bitcoin:'+code+'?amount=0.5&label=MathHarbour.com">\n <img src="https://sites.google.com/site/mathharbour/search/qrCode_mh.gif" ></a> \n <p>1C4RJcTeLBdStZNw8rXe2z4ev1UC1QVXF7</p>\n </div>'

textQr='<img src="http://ansrv.com/png?s=http://blockexplorer.com/q/getreceivedbyaddress/'+code+'&amp;c=000000&amp;b=FFFFFF&amp;size=5" />'

print('\n'+image+'\n\n')

print(textQr)
