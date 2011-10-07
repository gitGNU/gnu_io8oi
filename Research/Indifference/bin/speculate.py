#!/user/bin/python


"""
Description: reads data
111;222
333;444
.......
"""

files = ["fund.csv", "fund2.csv", ..., "fundN.csv"]


for f in files:

   fNew = file("."+f,"w")
   f = file(f).readlines()
   f.write([x.strip().split(";")[1] for x in f[-100:-1]])
   fNew.close()
