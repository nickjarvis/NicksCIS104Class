#print("Exersize 6.5")

text = 'X-DSPAM-Confidence: 0.8475 '

ipos = text.find(':')
#print(ipos)
piece = text[ipos+2:]
#print(piece)
#print(piece+42)will not work
value = float(piece)
print(value)
#print(value+42.0)
