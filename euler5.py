# Luis Navarro. 01-03-2018
# Adapted from Declan Reidy in the course forum (https://learnonline.gmit.ie/mod/forum/discuss.php?d=13330#p23461)
# Exercise 4 - Euler problem 5: 
#
# 2520 is the smallest number divisible by all numbers 1 to 10

i = 2520

for i in range(i,(20*19*18*17*16*15*14*13*12*11),20):
  if (i % 20 ==0) and (i % 19 ==0) and (i % 18 ==0) and (i % 17 ==0) and (i % 16 ==0) and (i % 15 ==0) and (i % 14 ==0) and (i % 13 ==0) and (i % 12 ==0) and (i % 11 ==0):
    print("The smallest number is:",i)
    break

