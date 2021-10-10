n = 10
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

for i in (5, 4, 3, 2, 1):
    print(i)
print("blastoff again")

zork = 0
print("before", zork)
for thing in (9, 12, 51, 20, 4, 72, 39) :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15, 78]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15, 1]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

#average
count = 0
sum = 0
print('Before:', count, sum)
for value in [3, 41, 12, 9, 74, 15, 78]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)

#accumulator
#  A variable used in a loop to add up or accumulate a result.
#counter
#  A variable used in a loop to count the number of times something happened. We initialize a counter to zero and then increment the counter each time we want to “count” something.
#decrement
#  An update that decreases the value of a variable.
#initialize
#  An assignment that gives an initial value to a variable that will be updated.
#increment
#  An update that increases the value of a variable (often by one).
#infinite loop
#  A loop in which the terminating condition is never satisfied or for which there is no terminating condition.
#iteration
#  Repeated execution of a set of statements using either a function that calls itself or a loop.
