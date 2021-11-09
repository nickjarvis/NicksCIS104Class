fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
#    print(line.rstrip())
    s = (line.split())
    for word in s:
        if word in lst:
            continue
        lst.append(word)
print(sorted(lst))
