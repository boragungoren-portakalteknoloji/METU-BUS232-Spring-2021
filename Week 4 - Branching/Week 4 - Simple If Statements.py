# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# The concept of branching enables the programmer to execute
# alternate logics, so that the program's behavior is altered.
# Some branches may exhibit larger changes such as exiting a program. 

greetings = "This program calculates Adult BMIs. If you are not an adult you should not continue."
question = "What do you want to do? (C)ontinue or (E)xit?"
print(greetings)
choice = input(question)
choice = choice.capitalize() # Now it does not matter c or C

# result = choice.startswith("C")
# if result:
if choice.startswith("C"):
    # ^ boolean expression ^ note the colon here
    print("Continuing as selected.")
    # print("Additional line.")
    # ^ note the indentation
else:
    # ^ note the colon here too.
    # else part is optional
    quit("Exiting as selected.")
        # ^ Message goes to the operating system, and logged. 
    # ^ note the indentation here too

# BTW we do a lot of string comparisons in branching. You should learn to use related Python string functions
# Take a peek at these three pages. Might come in handy in your homeworks or exams. 
# Upper/lower case processing -- https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
# String comparison -- https://www.geeksforgeeks.org/string-comparison-in-python/
# Contains another string -- https://www.geeksforgeeks.org/python-check-if-substring-present-in-string/

# The program calculates BMI using the kg/m2 formula. 

# We use if statements for a lot of input pre-processing.
# Well formatted inputs prevent errors. So we check the inputs for formats. 
weight = float ( input("Please enter your weight in kg.") )
        # Checking numbers, especially floats is a bit more tricky. So we skip in this example
height = float ( input("Please enter your height in cm.") )
shorter = input("Do you usually consider yourself as shorter than others? (Y/N)")
shorter = shorter.upper()[0]
#               ^ How does this work?
# shorter.upper() converts "yes" into "YES"
# [0] extracts "Y" from "YES"
# We expect either "Y" or "N" from this process. 
if shorter != "Y" and shorter != "N":
    # The and operator is a logical operator, its siblings or, not are also very popular
    # LHS and RHS - LHS shorter != "Y", RHS shorter != "N"
    # Result is true only when both sides hold true. when it is not Y and also it is not N.
    # See -- https://realpython.com/python-operators-expressions/#logical-operators
    # These operators exist in all programming languages
    print("Invalid choice. Assuming you are shorter than others. ")
    shorter = "Y"

heightMeters = height / 100.0;
BMI = weight / (heightMeters * heightMeters)

# The if statement or the else part can include nested if statements as well.
# The if else if ... else structure is an elegant outcome of this
# In Python we use the keyword elif for else if

if BMI < 18.5:
    # < has siblings >, <= and >=
    # They all return a boolean value
    print("You are underweight. Maybe you should put on some healthy weight.")
elif BMI < 25:
    print("Wonderful. You are at a healthy weight level.")
elif BMI < 30:
    print("Be careful. You are overweight. Watch what you eat.")  
elif BMI < 40:
    # Obese but not morbid obese
    print("You are very overweight. ")
    print("Please consult a health professional to lose weight.")   
    if "Y" == shorter:
        #  ^ == (equals) operator compares content of two objects, its sibling is != (not equals).
        # There is also a related operator called is. Used as if "Y" is shorter:
        # But is operator compares if the objects are actually the same object. It is more strict. 
        print("You should consider your weight more seriously than taller people.")
else: # This means BMI > 40 #30
    #print("You are very overweight. ")
    #print("Please consult a health professional to lose weight.")   
    #if "Y" == shorter:
        #  ^ == (equals) operator compares content of two objects, its sibling is != (not equals).
        # There is also a related operator called is. Used as if "Y" is shorter:
        # But is operator compares if the objects are actually the same object. It is more strict. 
        # print("You should consider your weight more seriously than taller people.")
    #  Done with the nested if statement
    # if BMI > 40: # Morbid obese
    #    print("You are also at risk of heart attack, and carry larger risk for COVID-19.")
    #    print("You should start losing weight immediately.")
    print("You are at risk of heart attack, and carry larger risk for COVID-19.")
    print("You should start losing weight immediately.")
    #  Done with the nested if statement
#Done with the else part
print("Done with your BMI calculation. Take care.")

# equivalent structure
# if BMI < 18.5:
#     print("You are underweight. Maybe you should put on some healthy weight.")
# else:
#     if BMI < 25:
#         print("Wonderful. You are at a healthy weight level.")    
#     else:
#         if BMI < 30:
#             print("Be careful. You are overweight. Watch what you eat.")  
#         else:
#             if BMI < 40:
#                 print("You are very overweight. ")
#                 print("Please consult a health professional to lose weight.")   
#                 if "Y" == shorter:        
#                     print("You should consider your weight more seriously than taller people.")
#             else:
#                 print("You are at risk of heart attack, and carry larger risk for COVID-19.")
#                 print("You should start losing weight immediately.")

# The following lines tell the Operating System we are exiting successfully. 
import sys
sys.exit(0)
# Zero is the success code
# If your program crashes the exit code should be a negative number.