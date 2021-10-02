def computepay(hours, rate) :
    print ("computepay", hours, rate)
    if hours > 40:
       rg = rate * hours
       ot = (hours - 40) * (rate * 0.5)
       pay = rg + ot
    else:
       pay = hours * rate
    print("Returning",pay)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
fh = float(hrs)
fr = float(rate)

py = computepay(fh,fr)

print ("Pay:",py)
