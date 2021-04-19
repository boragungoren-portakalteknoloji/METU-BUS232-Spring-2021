# defining your own function
def calculateDistance(start, end):
    # assume start and end are tuples of dimension 2
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    distance = abs(x2-x1) + abs(y2-y1)
    return distance

def forwardDistance(coordinates):
    sum = 0
    index = 0
    length = len(coordinates)
    while index < length-1:
        start = coordinates[index]
        end = coordinates[index + 1] # careful with indexes at the end
        distance = calculateDistance(start,end)   
        print("Distance between ", start, " and ", end, " is ", distance)
        sum = sum + distance
        # move on to the next index
        index = index + 1
    # Done with while
    return sum

# The following is very neat code. 
coordinates = [(1,1), (1,5), (2,6), (4,6), (5,3) ]
sum = forwardDistance(coordinates)
# calculate return trip individually and add
# return trip starts from last point in the list
length = len(coordinates)
end = coordinates[0]
start = coordinates[length-1] # last
# the following also works
# start = coordinates[-1] # last
backwardDistance = calculateDistance(start,end)   
sum = sum + backwardDistance
print("Total distance is ", sum)
