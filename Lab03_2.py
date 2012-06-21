print "Ernest Pobee"

num = raw_input("Enter your number")
num = int(num)

i = 0
out =0
while (num != 0):
     ex = (num % 10) + 7 # find the modulo of the current number and add 7 to it
     num = num / 10  # set the new value of num
     print ex,
     i = i + 1                #increment i
