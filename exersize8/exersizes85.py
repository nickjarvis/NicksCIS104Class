fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From':
        continue
    count = count + 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
