# Dictionaries in Python
# Dictionaries are used to store data in key-value pairs.

# The first use of this ability is to store the qualities or features of some item together
# Note the way we define the dictionary object

my_account = {
    "owner" : "bora",
    "id" : 1234567,
    "balance" : 250.0
    }

print("Account number", my_account["id"], "is owned by", my_account["owner"], " and has a balance of", my_account["balance"])
print("Withdrawing 100.0 TL")
my_account["balance"] = my_account["balance"] - 100.0
print("New balance:", my_account["balance"])

# A second use is to group and classify items of same type with a tag or identifier
# This way we can conduct a search base on the tag / identifier.
# Google is like a mega-sized dictionary of the web

addresses = {
    "METU_Ankara" : "METU Dept. Of Business Administration 06531 Cankaya, Ankara, TURKEY",
    "METU_NCC" : "Dept. of Business Administration METU NCC Kalkanlı Güzelyurt TRNC",
    "Bilkent" : "Bilkent University Dept. of Computer Science Universiteler Mahallesi Cankaya, Ankara, TURKEY",
    "Home" : "Cankaya, Ankara, TURKEY",
    "Ankara_Office" : "Cankaya, Ankara, TURKEY",
    "Istanbul_Office" : "Besiktas, Istanbul, TURKEY",
    "NYC_Office" : "Wall Street NY, NYC, USA",
    "Munich_Office": "Auenstrasse, Munich, GERMANY"
    }

#There are two ways to access individual items in a dictionary.
# The first method is more straightforward, but might generate and error if the key does not exist
# selected_address=input("Please select your address tag:")
# if (addresses[selected_address] is None):
#     print("No such address")
# else:
#     print("Your address details for given tag: ", addresses[selected_address])

# The second method is more robust with key errors. 
selected_address=input("Please select your address tag:")
result=addresses.get(selected_address) # Preferred version
if result:
    print("Your address details for given tag: ", result)
else:
    print("No such address")

# Note that the general way to deal with errors in Python is the try except clause.
# You are not required to learn about it, but you will benefit from doing so. 

input("Press any key to continue...")
# The items in a dictionary can be of any type. So we could create multiple levels

generic_basket = {"yoghurt", "apples", "bananas", "cherry tomatoes", "lettuce", "jalapeno pepper", "mineral water"}
computer_upgrade_basket = {"ram", "cpu", "motherboard"}
home_improvement_basket = {"ladder", "drill", "paint"}

# Here each value is a list of the budget and the contents of the basket
baskets = {
    "generic" : [250.0, generic_basket], # mapping of string to list of one double and one set
    "computer_upgrade" : [7000.0, computer_upgrade_basket], # mapping of string to list of one double and one set
    }
# Let's also add an item
baskets["home_improvement"]=[2500.0, home_improvement_basket]

# We can iterate over a dictionary
# A side note. Until Python 3.6 dictionaries were unordered, like sets. From Python 3.7 on they are ordered like lists.
print("Displaying all baskets:")
for key in baskets:
    print("key: ", key, " , value: ",  baskets[key])
    current_basket = baskets[key]
    # Work with current basket
    # The current basket is a list. It is indexed.
    # current_basket[0] -> budget, a double value
    # current_basket[1] -> items in the baskets, a set of strings