print "Ernest Pobee"

theInput = raw_input("Enter an integer: ")
#Your code here

theInput = int(theInput)
if (theInput % 2 == 0):
     print "even"
else :
     print "odd"


print "------------------------------------------------------"

# Question 6

primary_school_age = 5
legal_voting_age = 18
president_eligible = 21
off_retirement_age = 60

personsAge = raw_input("Enter an age: ")
personsAge = int(personsAge)

if (personsAge < primary_school_age):
     print "Too young"
elif (personsAge >= legal_voting_age):
     print "Remember to vote"
elif(personsAge >= off_retirement_age):
     print "Too old"
elif (personsAge >= president_eligible):
     print "Vote for me"
else:
     print "You can't be president"


print "----------------------------------------------------"

# Question 7
print "while loop that prints out all the multiples of 3 down from 40 to 0 in decreasing order"
i = 40
while (i > -1):
     if (i % 3 == 0):
          if(i == 0):
               print i
          print i,","
     i = i-1



print "------------------------------------------------------"

# Question 8
print "Write a loop that prints out all numbers between \n6 and 30 that are not divisible by 2, 3, or 5.\n"
i = 6
while (i <30):
     if (i % 2 != 0):
          if(i % 3 != 0):
               if (i % 5!= 0):
                    print i
     i = i +1

print "---------------------------------------------------------"

# Question 9

n = 1
while (n):
     a = 79*n
     if ( a % 97 == 1 ):
          print "The smallest possible integer is ",n
          break
     
     n = n + 1

print "----------------------------------------------------------"
