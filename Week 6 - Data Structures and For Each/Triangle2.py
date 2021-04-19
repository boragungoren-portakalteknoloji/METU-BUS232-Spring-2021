import math
# There is a bunch of functions in math -- https://docs.python.org/3/library/math.html

def createpoint(pointnumber):
    print("Processing point", pointnumber)
    x = float ( input("Enter x:") )
    y = float ( input("Enter y:") )
    point = (x,y)
    return point

def distance(point1, point2):
    # assume points are 2-tuples
    deltax = point1[0]-point2[0]
    deltay = point1[1]-point2[1]
    dist = math.sqrt(deltax*deltax + deltay*deltay)
    return dist

pointa = createpoint("a")
pointb = createpoint("b")
pointc = createpoint("c")

distab = distance(pointa, pointb)
distbc = distance(pointb, pointc)
distca = distance(pointc, pointa)

perimeter = distab + distbc + distca
print("Perimeter is:", perimeter)

