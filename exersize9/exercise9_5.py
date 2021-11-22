dictionary_domains = dict()
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
        atpos = words[1].find('@')
        domain = words[1][atpos + 1:]
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1
        else:
            dictionary_domains[domain] += 1
print(dictionary_domains)
