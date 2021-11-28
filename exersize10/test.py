import re

with open ('regex_sum_1359183.txt') as file:
    num = file.read ()
y = re.findall('[0-9]+', num)
#print (y)
newlist = []
for i in y :
    if i :
        i = int(i)
        newlist.append(i)
print(sum(newlist))
