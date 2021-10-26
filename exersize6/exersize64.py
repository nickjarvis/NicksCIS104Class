




#count = 0
#for letter in word:
#    if letter == 'letterin':
#        count = count + 1
#    print(count)

def count(letterin):
    counter = 0
    word = 'banana'
    for letter in word:
        if letter == letterin:
            counter = counter + 1
    print(counter)
letterin = input('Enter letter: ')
count(letterin)
