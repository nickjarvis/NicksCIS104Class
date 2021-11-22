
dictionary_addresses = dict()
name = input('Enter a file: ')
try:
    fhand = open(name)
except FileNotFoundError:
    print('File cannot be opened:', name)
    exit()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1

print(dictionary_addresses)
