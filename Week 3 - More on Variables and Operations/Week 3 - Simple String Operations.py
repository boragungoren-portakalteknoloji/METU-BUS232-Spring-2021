# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# Splitting may appear complex but is really simple
combinedname = "bora güngören"
# ^ variable type becomes a string and it comes with its operations
# <variable name>.operationname(...)
parts = combinedname.split() # "bora" and "güngören"
#                   ^ . means call
#                    split operation on yourself
#       split ends with a series of smaller strings, and packs them into
#       a "structure." LEt's just say it is indexed, there are positions of the smaller strings.
name, surname = parts[0], parts[1]
#               [] - brackets denote access to one particular smaller string
#               number inside the bracket is the position, positions start with zero
#               parts[0] -> "bora", parts[1] -> "güngören"
print("Name:", name, " and Surname:", surname)

# Capitalize first letter
name = name.capitalize()
#          ^ call capitalize()
#          capitalize takes a clone, capitalizes it and returns
# name = <capitalized return>
# we assign the changed version over the old version
surname = surname.capitalize()
print("Name:", name, " and Surname:", surname)

# Capitalize all letters
surname = surname.upper()
#                ^ upper() capitalizes all letters
print("Name:", name, " and Surname:", surname)

# Concatenate two strings
formalname = surname + ", " + name
print("Formal specified name:", formalname)

#Concatenate string with number
pilotcallsign = "Red" + str(5)
# convert number to string using str(), sibling of int() and float() 5 -> "5"
print(pilotcallsign, ", Do you copy?")