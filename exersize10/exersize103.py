import string

counts = 0                          # Initialize variables
dictionary_counts = dict()
relative_lst = list()

name = input('Enter file: ')
try:
    fhand = open(name)
except FileNotFoundError:
    print('File cannot be opened:', name)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:

            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_lst.append((val / counts, key))

relative_lst.sort(reverse=True)

for key, val in relative_lst:
    print(key, val)
