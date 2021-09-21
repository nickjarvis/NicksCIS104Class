hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
ab = float(rate)
if (h) > 40:
  ot= (h - 40)
  #print (ot)
  ac= (ab * 1.5)
  #print (ac)
  af= float(ac) * float(ot)
  #print (af)
  ae= (ab) * 40
  #print (ae)
  ef= float(ae) + float(af)
  print (ef)
else:
  pay = (h) * (ab)
  print ("Pay:",pay)
