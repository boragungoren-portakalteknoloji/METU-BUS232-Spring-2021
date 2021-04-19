import math
# There is a bunch of functions in math -- https://docs.python.org/3/library/math.html

def createpoint(pointnumber):
    # ^ def name is searched by the function call.
    # createpoint("a") -> pointnumber = "a"
    # createpoint("b") -> pointnumber = "b"
    # The function call is told to have its own "scope". Scope means the variables accessible.
    # The function call access the variable pointnumber, and it has the value presented in the call
    # for example createpoint("a") is the call
    # Lines indeted in the definition are executed each time there is a call. (Goal achieved. No more copy and paste)
    print("Processing point", pointnumber)
    x = float ( input("Enter x:") )
    y = float ( input("Enter y:") )
    point = (x,y)
    return point
    # ^ the return keyword lets the scope return to where it was before the function call
    # it also returns the value next to it, and replaces it with the function call

def distance(point1, point2):
    # assume points are 2-tuples
    deltax = point1[0]-point2[0]
            #  ^ access to the 0th / first item in the tuple
            # pointa = (x1,     y1)
            #           ^ 0th,  ^ 1st
            #           there are zero items before this item
    deltay = point1[1]-point2[1]
            # ^ access to 1st item
            # there are 1 items before this item
    dist = math.sqrt(deltax*deltax + deltay*deltay)
    return dist

pointa = createpoint("a")
        # ^ Function call. The variables or values b.w. paranthesis are sent towards the "definition"
        # Code in the definition is executed on the variables or values sent.
        # Return statement in the function definition returns a value like (1,1)
        # pointa = (1,1) can run
pointb = createpoint("b")
        # when i copy and paste a function call, the variables are stressed.
        # it is easier and more reliable to change the variables "once" in the call
        # than change every occurence of variables in the code we moved into the function definition
        # When is it more beneficial? Larger code segments, complex code segments, very similar variable names
pointc = createpoint("c")

distab = distance(pointa, pointb)
            # ^ in this call, points already have the x's and y's inside them. Logically we are
            # calculating the distance b.w. points.
            # the definition when executed ends with return dist
            # the value there is assigned on to distab
            # distab = 1.4....
distbc = distance(pointb, pointc)
distca = distance(pointc, pointa)

perimeter = round (distab + distbc + distca, 2)
print("Perimeter is:", perimeter)

# Triangle.py and Triangle2.py are equivalent in the sense that they do the exact same thing.
# Exact same inputs, exact same outputs irrespective of the inputs.
# Triangle2 which uses 2 function definitions is superior in the sense that it is more organized.
# More organized code is easier to check for errors and correct them.
# Errors in the function definition get to be corrected just once.
# Not making a mistake is always cheaper than correcting a mistake.
# Correcting a mistake early is much cheaper than correcting the same mistake late
# Functions isolate mistakes in their scopes, and make it cheaper to correct mistakes.
# As a student cheaper means in shorter time, as a company time -> money.
