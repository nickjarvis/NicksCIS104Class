#word = 'banana'
#count = 0
#for letter in word:
    #if letter == 'a':
        #count = count + 1
#print(count)



def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)
wordin = input('Enter word: ')
letterin = input('Enter letter: ')
count(wordin, letterin)
