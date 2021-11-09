#fhand = open('mbox-short.txt')
#fhand = open('test.txt')
#count = 0
#for line in fhand:
#    words = line.split()
#    print('Debug:',words)
#    if len(words) == 0 : continue
#    if words[0] != 'From': continue
#    print(words[2])




#fhand = open('mbox-short.txt')
fhand = open('test.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
