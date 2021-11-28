dictionary_hours = dict()               # Initialize variables
lst = list()

name = input('Enter file: ')
try:
    fhand = open(name)
except FileNotFoundError:
    print('File cannot be opened:', name)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    colpos = words[5].find(':')
    hour = words[5][:colpos]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1
    else:
        dictionary_hours[hour] += 1

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
