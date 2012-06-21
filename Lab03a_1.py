print "Ernest Pobee"

num = raw_input("Enter your number")
num = int(num)

i = 0
out =0
while (num != 0):
     ex = num % 10 # the number entered modulo 10
     num = num / 10      #set new value of num
     print ex,
     i = i + 1                #increment i
