import math # importing a library

x1 = float ( input("x1:") )
y1 = float ( input("y1:") )
pointa = (x1,y1)
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
distance2 = math.sqrt( (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3) )
distance3 = math.sqrt( (x3-x1)*(x3-x1) + (y3-y1)*(y3-y1) )

perimeter = distance1 + distance2 + distance3
print("Perimeter is:", perimeter)
