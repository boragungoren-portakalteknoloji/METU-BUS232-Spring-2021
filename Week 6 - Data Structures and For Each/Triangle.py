import math # importing a library

x1 = float ( input("x1:") )
y1 = float ( input("y1:") )
pointa = (x1,y1)
#         ^ packed together as a single structure
#  the variable pointa is used to access the structure
print(pointa)

x2 = float ( input("x2:") )
y2 = float ( input("y2:") )
pointb = (x2,y2)
print(pointb)

x3 = float ( input("x3:") )
y3 = float ( input("y3:") )
pointc = (x3,y3)
print(pointc)

distance1 = math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )
#                        ^ x1, x2, etc are always available
#                        they are located in the structure. like sitting in a car.
distance2 = math.sqrt( (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3) )
#             ^ from the math library the sqrt function
#               call from a library installed on the computer the program runs.
#               math is a standard library so it is installed with python
distance3 = math.sqrt( (x3-x1)*(x3-x1) + (y3-y1)*(y3-y1) )

perimeter = round( distance1 + distance2 + distance3, 2)
#                                                     ^ number of digits after decimal point
print("Perimeter is:", perimeter)
