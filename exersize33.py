score = input("Enter Score: ")
sc = float(score)
if sc <= 0.6:
  print ("F")
elif 0.6 < sc <= 0.7:
  print ("D")
elif 0.7 < sc <= 0.8:
  print ("C")
elif 0.8 < sc <= 0.9:
  print ("B")
elif 0.9 < sc <= 1.0:
  print ("A")




#.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
