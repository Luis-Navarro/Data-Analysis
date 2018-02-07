# Luis Navarro, 06-Feb-2018
# Collatz Conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture

i = int (input ("Please enter a starting integer for testing Collatz Conjecture: "))
if (i<0):
    print "Collatz Conjecture implies using positive integers"
    i = 1
        
j = 0
while (i != 1):
    if (i % 2 == 0):
        i = i/2
    elif (i % 2 != 0):
        i = i*3 + 1
    print (i)
    j = j+1

print ("It took "),  (j),  ("steps to get to 1")
