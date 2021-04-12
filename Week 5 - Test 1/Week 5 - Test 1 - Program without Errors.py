# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# The following program wii calculate an expected value from three user input
# The inputs are the lesser likely minimum value, the lesser likely
# maximum value and the most likely value. They are given pre-determined
# weights of 1, 1, and 4 respectively.

print("This program will calculate an expected value. ")
print("You will be prompted for three inputs, all should be numbers.")
minValue = float ( input("Please input the lesser likely minimum value. ") )
maxValue = float( input("Please input the lesser likely maximum value. ") )
mostLikelyValue = float ( input("Please input the most likely value. ") )

if minValue == mostLikelyValue and maxValue == mostLikelyValue:
    print("They are all the same.")
elif minValue == mostLikelyValue:
    print("You have also assumed that the minimum value is the most likely value")
elif maxValue == mostLikelyValue:
    print("You have also assumed that the maximum value is the most likely value")
    
expectedValue = round ( (1.0 * minValue + 4.0 * mostLikelyValue + 1.0 * maxValue) / 6.0, 2)
print("The expected value is: ", expectedValue)
