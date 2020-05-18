str = 'X-DSPAM-Confidence: 0.8475 '
#sval = str[19:26]
#fval = float (sval)
#print (fval)

ipos = str.find(':')
print(ipos)
piece = str[ipos+1:]
print (piece)
value = float (piece)
print (value)
