# High quality water has a ph level slightly less than 7
# Also a high quality water source has stable ph levels. If it is more than 7 it should be more than 7 always.
# Because the change in the ph level signifies something has changed in the water level. 
def calculateAverage(listOfDatapoints):
    sum = 0
    for datapoint in listOfDatapoints: # repeats tasks for all items in list
        # because this runs for each and every one of the items
        # we usually call this a for-each. Read as for each datapoint in list of datapoints.
        # For-each iterates automatically from start to finish
        sum = sum + datapoint
    avg = sum / len(listOfDatapoints)
    return avg

phlevels = [7.1, 7.5, 7.3, 6.9, 7.2, 7.4, 7.2, 7.4, 6.9, 6.8, 5.0, 5.1, 5.9]
#          ^------------------------------------------------^ ^----------^
#                      ^ 0, 1, ..., len -4                       ^ len -3, len -2 , len -1
#                      start with 0 and always less than len-3    ^ start with len-3 always less than len
# calculate avg of all data except past (latest) three
# then calculate avg of laterst three.
# Compare. If deviation is more than %10 there is a significant deviation.

# Problem 1 - How do I identify the two parts with indexes?
#       - Answer phlevels[start:limit] so that indexes start with start and are less than limit
# Problem 2 - How do I calculate an average in an index range?
#       - Answer use a for-each

length = len(phlevels)
# part with indexes 0, 1, ..., length-4 (inclusive)

olddata = phlevels[0:length-3] # start from zero less than length-3
# olddata = phlevels[:length-3] # first one empty means from start
# This creates a new list (a copy) that can access the part of the list we had
print(olddata)
avgOld = calculateAverage(olddata)

# calculate avg of past (latest) three
latestdata = phlevels[length-3:] #second one empty means to the end
# This creates  a new list
print(latestdata)
avgLatest = calculateAverage(latestdata)

# calculate deviation (absolute)
devAbs = abs(avgLatest - avgOld)
# calculate deviation (percent)
devPercent = devAbs / avgOld
# if deviation is > %10 (0.10) then sound an alarm
if devPercent > 0.10: # conditional code execution
    print("Quality control alarm!")
    percent = round( devPercent * 100.0, 2)
    print("Deviation is,", percent,"percent.")
else:
    print("All is OK")

# When use for-each but not while?
# For each is more suitable when we consume all items in a list one by one
# And when we have no relation to consider between the items so that items are really individuals.
# In the jogger example, distances were a product of the relationship between points.
# So to conceptualize the distance we needed two points. One point alone would not be enough. So not a problem for for-each.
# In the water quality, the problem can be solved by conceptualizing the average as a summation of individual values divided by size
# Here the loop can be constructed with the assumption of no relation between items in the list. So suitable for for-each.
