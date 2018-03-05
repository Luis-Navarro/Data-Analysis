# Luis Navarro 05-03-2018
# factorial function

def factorial(x):
    prod = 1
    for i in range(1, x + 1):
        prod = prod * i
    return prod

print ("The factor of 5 is: ", factorial(5))
print ("The factor of 7 is: ", factorial(7))
print ("The factor of 10 is: ", factorial(10))
