# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# The following program wii calculate an expected value from three user input
# The inputs are the lesser likely minimum value, the lesser likely
# maximum value and the most likely value. They are given pre-determined
# weights of 1, 1, and 4 respectively.

print("This program will calculate an expected value. ")
print("You will be prompted for three inputs, all should be numbers.")
minValue = input("Please input the lesser likely minimum value.")
maxValue = input("Please input the lesser likely maximum value.")
mostLikelyValue = input("Please input the lesser most likely value.")

if minValue == mosLikelyValue:
print("You have also assumed that the minimum value is the most likely value")
elif maxValue == mosLikelyValue:
    print("You have also assumed that the maximum value is the most likely value")
    
expectedValue = (1.0 * minValue + 4.0 * mostLikelyValue + 1.0 * maxValue) / 6.0
print("The expected value is: ", expectedValue)
