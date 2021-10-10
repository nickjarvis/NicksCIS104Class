count = 0
sum = 0.0
while True :
    sval = input('Enter a Number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    count = count + 1
    sum = sum + fval

#print('ALL DONE')
print(count, sum, sum/count)
