#fh = open ('mbox-short.txt')
#for lx in fh:
#    ly = lx.strip()
#    print (ly.upper())

fname = input ( 'enter name : ')
try:
    fhand = open(fname)
except:
    print ('file can not be opened:', fname)
    quit()
count = 0
totalspam = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        sp = line.find (" ")
        thenum = float(line[sp+1:])
        totalspam += thenum
        count += 1
print("Average spam confidence:", totalspam/count)
