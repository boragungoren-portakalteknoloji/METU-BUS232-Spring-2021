# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# Let's begin with some basics
a = 2
b = 3
c = a + b
print("a:",a,"b:",b,"c:",c)

# So how did this work?
# operator+ (summation) works and its result is passed as RHS of operator= (assignment)
# operator= assigns the results to variable c.
# Values of a and b are not changed.

# Then some more calculations
c = a * b + b * c # Multiplication is done before summation
#   2 x 3 + 3 x 5
#   6 + 15
#   21
print("a:",a,"b:",b,"c:",c)

c = ( a - 1) * b # Paranthesis is done before all
#    1 * 3
#    3
print("a:",a,"b:",b,"c:",c)

c = a / b # Division is not necessarily yielding an integer value
#   the result is floating point value
# Because Python is dynamically typed, c becomes a floating point (real number) variable
print("a:",a,"b:",b,"c:",c)

# See if you explicitly make a and b integers
a = int(2)
b = int(3)
c = a / b # Division is not necessarily yielding an integer value again
print("a:",a,"b:",b,"c:",c)

# So if you want to have an integer value for the result, convert it
c = int( a / b) 
print("a:",a,"b:",b,"c:",c)

# Integer conversion is not rounding
c = -1.5 # -1.5 should be rounded to what?
print("c:",c, "int(c)",int(c))

# For rounding, there are many methods.
# See - https://realpython.com/python-rounding/

# Math operations
# 1- Order: Paranthesis, mult/div over add/subtract, left over right when equal
# 2- Type of result: Integers divided can end up as floats

a = 2.0 # a became a float
b = 3.0 # b became a float
c = a + b
print("a:",a,"b:",b,"c:",c) # 5.0 in the output means c became a float

d = c + 1 # c is a float, 5.0 and 1 is an integer
print("d:",d)

# e = d / 0 # divide by zero crashes your program
# ZeroDivisionError: float division by zero

e = d / 0.00000000001 # divide by near-zero does not crash your program
print("e:",e)

f = 5.0001
g = 4.9999
difference = f - g # floats are not necessarily exact
print ("difference:", difference)
e = d / difference
print("e:",e)
# Many people round the result of float operations