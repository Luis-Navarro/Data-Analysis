# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# My name is Luis, so L=12 and S=19. They add up to 31 
x = 31
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# This part returns the Fibonacci number of the ASCII code taken from my surname's first and last letters added together.
name = "Navarro"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
