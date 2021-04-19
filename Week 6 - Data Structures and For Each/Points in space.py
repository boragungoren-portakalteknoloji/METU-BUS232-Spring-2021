x = 1
y = 3
point = (x,y) # tuple
# ^ Similar to Triangle. Items were of the same type.
# The tuple was used to order items of the same type (here numbers).
print ("My first point is:", point)
print ("0th item in tuple is:", point[0]) # <- 0 implies the order
print ("1st item in tuple is:", point[1]) # <- 1 implies the order

id = ("Bora", "Güngören", 1234567, "gbora@metu.edu.tr")
#      ^ String   ^ String   ^ Integer ^String

coordinates =( (0,0)  , (1,1) )
#               ^ tuple   ^ tuple
pointDimension = len(point)
                # ^ len calculates the number of items in the structure, here 2.
                # the indexes used to access items start with 0, so they are always less than the output of len
                # 0,1 < 2 
print("Our point is ", pointDimension, " dimensioned.")

point2 = [x,y]
        # ^ no parantheses but brackets. A list is created with brackets.
print ("Second point, as a list is:", point2)

converted = list (point) # converts tuple or any similar structure to a list
print("Converted from tuple to list:", converted)

# A tuple cannot be created empty and than filled.
# A list can be created empty and then items can be added and removed

# List is very flexible in terms of adding/removing items.
# Items can be added/removed one by one or in groups.
# Learning about lists is very important in Python and generally programming
# Use lists to conceptualize groups, stacked items, queues, etc.
# It is the most common abstract data type becayus it abstracts many common operations

emptyList = []
#           ^ Lists are created by brackets. This is how to differentiate them in code from tuples.
print(emptyList)
# printing an empty list just shows the brackets and nothing in between
input("press any key to continue")

emptyList.append(point)
# Appending an item appends it in the back like a tail.
# Here: [ ] appended by (1,3) becomes [ (1,3) ]
# The item inside the list is a tuple. 
print(emptyList)
# [ (1,3) ] is a list because of [] which contains (1,3) which is a single tuple
input("press any key to continue")

emptyList.append( (2,5) )
# Here: [ (1,3) ] appended by (2,5) becomes [ (1,3) , (2,5) ]
# This is a list containing two "ordered" tuples. The ordering is (1,3) before (2,5).
# Hence the indexes 0 and 1 assigned. 0 index -> (1,3), 1 index -> (2,5)
# The lenght of this list is 2, which is always bigger than 0 or 1 (the indexes)
print(emptyList)
input("press any key to continue")

emptyList.append( (6,9) )
# Here: [ (1,3) , (2,5) ] appended by (6,9) becomes [ (1,3) , (2,5) , (6,9) ]
# The indexes 0, 1, 2. 2 is assigned to (6,9)
print(emptyList)
input("press any key to continue")

emptyList.extend( [ (5,9),(9,5)])
# Here the extend function parameter is [ (5,9), (9,5)] which is another list
# [ (1,3) , (2,5) , (6,9) ] is extended by [ (5,9), (9,5)]
# Becomes [ (1,3) , (2,5) , (6,9) , (5,9), (9,5)]
# Appending an item is done by append()
# Appending a whole list is done by extend()
print(emptyList)
input("press any key to continue")

copy = emptyList.copy()
print("Empty list is not so empty now: ", emptyList)
print("The copy is: ", copy)

# Usually a tuple is used to collect related items together and implies an unnamed type
# METU Personnel/Student ID - ("Bora", "Güngören", 1234567, "gbora@metu.edu.tr")
# A list is used to collect variables of the same type to process them together
# Example. There is a list of student IDs. The IDs are all of the structure above (4 items, last one is the email).

# Go over each entry in the list.
#   For the current entry, extract the value for the email address.
#   Send the email to the extracted email address from the current entry.
# This program description is irrelevant of "size"

# Considering "size" in computers you can work things through induction.
# So whatever works for 2 items, may work for 3, 4, ....... up to the capacity of your physical computer hardware
# Quote this to your instructor. "There are three numbers in computing. 0, 1, and infinity".

# The tool to "go over each entry in the list" is called a "loop"