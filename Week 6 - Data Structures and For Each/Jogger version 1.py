# Calculate the forward distance in terms of Manhattan distance (not Euclidean)
# When going through a path
coordinates = [(1,1), (1,5), (2,6), (4,6), (5,3) ]
# ^ This is a list of tuples. 5 tuples with indexes 0,1,..,4
sum = 0
# ^ represent the total distance covered
print (coordinates[0])
print (coordinates[1])
# index from 0 to 4 (inclusive)
# index from 0 and always less than 5 (length of list)

# summation the results
# distance from 0 to 1 - > index is 0, index+1 is 1
# distance from 1 to 2 - > index is 1, index+1 is 2
# ...
# distance from 3 to 4 - > index is 3, index+1 is 4

# idea: distance between coordinates[index] and coordinates[index + 1]
# 1- abstract the indexes and how they are incremented into a variable called index
# in this case, the value of the variable index goes from 0 to 3
# 2- now abstract the value range, 0 and 3 in terms of the properties of the structure (i.e. list)
# 5 is the size. and 4 is size -1, 3 is size - 2
# 0, ....3 is from 0 to size -2 which are all, always less than size - 1 (which is 4)
# if I can express in terms of "size" or "length" than my program can adapt to different sizes. 
# 3- If only I had a programming language construct that allowed me to go over all those values?

# The loop is an extension of the if structure.
# If connects to alternative branches in the future, in the code ahead.
# A loop takes a branch and connects it to just before it started. So that the loop can be repeated many times.
# The condition checked on if decides which branch to take.
# The condition in a loop decides whether to go back, or stop looping (i.e. break the loop).

# 3- what is our condition? Use the index. We will calculate distances and add the distance to the sum
# as long as we have more stops to cover.
# index is 0. I have 1 to go.
# index is 1. I have 2 to go.
# index is size/len-2 I have size/len -1 to go.
# index is size/len-1 (I am at the last stop) so I have nowhere to go. I stop / break from the loop.
# the condition to continue is therefore index < size/len-1 (in this case where len is 5, it becomes index < 4

index = 0
length = len(coordinates) # here length is 5, length -1 is 4.
while index < length-1:
    # as long as the condition here holds true, the code indented will be executed
    start = coordinates[index]
    end = coordinates[index + 1] # careful with indexes at the end
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    distance = abs(x2-x1) + abs(y2-y1) # Manhattan distance formula
    print("Index is", index)
    print("Distance between ", start, " and ", end, " is ", distance)
    sum = sum + distance
    # move on to the next index
    index = index + 1
# out of indentation = out of while
print("Forward distance is ", sum)
print("Index after loop is", index)

# calculate return trip individually and add
# return trip starts from last point in the list
end = coordinates[0]
start = coordinates[length-1] # last
# the following also works
# start = coordinates[-1] # last
x1 = start[0]
x2 = end[0]
y1 = start[1]
y2 = end[1]
distance = abs(x2-x1) + abs(y2-y1)
sum = sum + distance
print("Total distance is ", sum)

# The while loop is fitted best to cases where we try to consume things.
# In this example we consumed pairs of points until we run out of points.
# While there are "pairs of points left to consume"
# Reading a file filled with records. We consume one record at a time. A while loop
# designed to consume record while "there are records left to consume" will fit.
# If you can conceptualize a loop as a consumption problem, and find the logical test
# such as index < length-1 then you are OK with a while. 