# This is a comment line. It is intended for the human reader to read and understand code.
# A file is the typical unit of program construction. It should be perceived as a "physical" unit
# whereas the logical breakdown of the program could be different, spanning and cross-cutting files 
# At the beginning of each program file, a license type, and a list of developers/authors are usually specified. 
# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

print("Hello World") # This is also a comment.
# ^ print is a default library supplied function, it usually takes a textual/String parameter which is delimited by the quotation marks
# So in this case "Hello World" is the parameter

print("The author of this program is", "Bora Güngören")
# Print also uses a comma between multiple parameters, however they end up consecutive in a line

print("First line\nSecond line")
# print("First line\n", "Second line") # This is a commented program line, it does not work. 
# The \n is a special character that symbolizes the end of line, therefore the output moves to the next line instead of printing something
# There are some other special characters like that: One of them is \t which is the tab character. It will become very useful in your course.
print("There is a tab in between \t can you notice it?")
print("Look what the tab does to text that looks like columns:")
print("First\tSecond\tThird")      
print("12\t3455\t120")

# One other important use will be about formatting your Python code. Tabs vs spaces is an eternal debate among programmers.
# We will enter the debate on tabs vs spaces on Week 4, just before Test 1. 
# For a serious discussion -- https://wiki.c2.com/?TabsVersusSpaces
# For a really funny sketch about it -- https://www.youtube.com/watch?v=V7PLxL8jIl8

# For more examples on print, visit -- https://realpython.com/python-print/

# Now we will read some input from the user.
# There are a number of stuff to dicuss here. Let's first run the lines
userinput = input("Type anything and press enter: ")
# When the user types anything this gets converted to
# userinput = "anything" 
print("Your input was:", userinput)

# userinput = input("Type anything: ")
# In this line the right hand side of = works first. This is always like this with a line with =
# We call the = sign as "the assignment operator" in Python and many programming languages.
# It lets the right hand side (RHS) to execute, and gets the results as a value
# Then it assigns the RHS "value" to the named variable on the left hand side (LHS)
# So it works as LHS <----- RHS result

# Returning to input(), it is also a default library defined function
# It is called using a prompt message you supply. In this case it is "Type anything and press enter: "
# When the user types something and presses enter, the text from the standard input device (usually the keyboard) gets to be formatted as a text/String value


# Returning to the assignment operator, 
# userinput = input("Type anything: ")
# When we assign that value to the named variable userinput, the value is now accesible through the variable's name. 
# Therefore it is printable
# print(userinput)

# There are many types of values. However because the input mechanisms are usually based on text, we struggle to understand what text means to us. 
# More details in input and output -- https://docs.python.org/3/tutorial/inputoutput.html
# and -- https://realpython.com/python-input-output/

# This week we will have Homework #2. Next week's Homework #3 will be about formatting.
# To be ready for HW #3, you can complete the tutorial on -- https://realpython.com/python-string-formatting/
