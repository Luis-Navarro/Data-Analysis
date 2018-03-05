# Python Exercises

##fib1.py
It includes both parts taken from the course. First, it calculates de 31st Fibonacci number, based on the manual addition of the first and last letters in my name, based on their alphabetical order. The second part, automates this process with my surname. The script determines which is the first and last letters of my complete surname, then returns the ASCII codes for those characters through ord(). Once done, it adds them up and calculates the Fibonacci number for the resulting number. 
This script was coded by Ian McLoughlin and uploaded to his github repository (https://github.com/ianmcloughlin/python-fib).

##collatz.py 
This was entirely coded by myself following instructions provided during the course. The Collatz Conjecture states that given any positive integer and performing the same arithmetical steps to calculate the following number in the series, it will eventually end in 1. This arithmetical steps are as follows: if the integer is even, divide by 2. If it is an odd number, multiply per 3 and add 1.
I added two features to this loop:
First, I introduced an input for the starting integer. Negative integer introduction is prevented by a simple 'if' statement and a warning 'print' output. It also transforms the negative input into '1' to skip the loop and end the script, preventing infinite looping.
The second contribution consisted in adding a counter of the required steps until Collatz Conjecture gets to 1. This 'j' variable is included in the loop with an incremental value. In that way, every time the loop is used, 'j' value is increased by 1.

##euler5.py 
This script is copied from Declan Reidy. After struggling with coding I found in the forum Declan's solution as a very short, straight-forward and mathematically consistent solution.

##factorial.py
Using function and a simple loop that multiplies in the given range.
