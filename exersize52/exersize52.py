largest = None
smallest = None
while True :
    num = input('Enter a Number: ')
    if num == 'done' :
        break
    #print(num)
    try:
        fval = int(num)
    except:
        print('Invalid input')
        continue
    #print(fval)
    if largest is None or fval > largest :
            largest = fval
    if smallest is None or fval < smallest :
            smallest = fval

print('Maximum is', largest)
print('Minimum is', smallest)
