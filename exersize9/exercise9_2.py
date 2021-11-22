
dictionary_days = dict()
name = input('Enter a file: ')
try:
    fhand = open(name)
except FileNotFoundError:
    print('File cannot be opened:', name)
    exit()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1
        else:
            dictionary_days[words[2]] += 1
print(dictionary_days)
