# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# The concept of a variable is very important
# In Python convention, variables are assigned values as they are created
aname = "Bora" # Declaration is to mention the variable name for the first time
anumber = 1979 # Definition is to assign the value to the variable
# Python convension is to declare and define at the same time

print("Here is a name:", aname, "and a number:", anumber)

# However, we can create a variable without an explicit value or
# un-assign the value given.
# This is done using the key word None. 

anothernumber = None # This variable is declared but not defined
anumber = None # Variables with value None are not safe to use in operations

print("A number:", anumber, "and another number:", anothernumber)

# In some languages, multiple variables can be defined in the same line like this
# a = 1, b = 2
# The Python way of doing this is as follows, It will become very useful
# some time later.
# At the time being, just know that it is possible to do it like this. 
apartmentnumber,apartmentname, doornumber = 1,"My Apartment",2
print("apartment number:",apartmentnumber,"door number:",doornumber)

# Name your variable so that (1) it explains the real world concept,
# (2) it gives a clue about the type (i.e. int, string)

# Here is a naming convention from the 1990s, uses and promoted by Microsoft
# i32_apartmentNumber

# The reason we have variables is to hold values in specific position in
# memory so that we can recollect them and process them.
# Low level data processing has very strict rules in computing. In order to
# easily manage these rules in our understanding, programming languages
# have the concept of a type. And they are classified as strongly-typed
# and weakly-typed languages. There are some typeless languages as well.
# Typing can also occur statically and dynamically.

# Python is a dynamically-typed language. That means the type of the variable
# is based not on the name but the content.

anumber = "Bora"
# Now is the variable anumber referring to a number?
print("Content of the variable anumber:", anumber)

# You could interpret this as switching/changing types, mutations, polymorphism, etc.
# That's the way it is. 
# It is therefore important to make sure the RHS of the assignment for
# a variable holds the correct type.

anumber = "1234"
# Is this a number or some text?
# For a short but correct explanation of this, you could refer to -- https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/
# Much longer and detailed explanations are available elsewhere. 
# type

# Here is an example from Java which is statically typed:
# int anumber = 1234; # This is fixed. You cannot change, hence statically

# Here is a way to explicitly express two common number types for an input
anumber = int("1234") # We switched the type of anumber
anothernumber = float("12.34") 

# How would you use this with CLI?
age = int ( input("What is your age:") )
#      ^ there is something (expression) inside my paranthesis so let it run first.
#             ^ input prompts the user, get the CLI, i.e. "350"
#             ^ input returns the CLI, "350" as a string
#      ^ int re-interprets the CLI "350" as 350, and integer number and returns that
#      ^ here is 350
# age = 350
# This type of conversion is called input pre-processing
print("You are", age,"years old.")

# We can learn the type of a variable with the library function type.
# Nevermind the verbosity of the output. Just focus on the keyword int
print("Data type of age:",type(age))

# When does this type concept matter? Por Python, not when we assign the values
# (because we could switch types), but when we use the values in the variables.

# We use the values in the variables with operations.

