# Sets in Python
# A set is a collection which is both unordered and unindexed.

simple_cart = {"yoghurt", "apples", "bananas", "cherry tomatoes", "lettuce", "jalapeno pepper", "mineral water"}
size = len(simple_cart)
print("Here is my shopping cart today:", simple_cart)
print("It contains", size, "items")

# Items in a set do not repeat themselves. So you cannot add them multiple times.
simple_cart.add("carrots")
simple_cart.add("apples")
print("Here is my updated shopping cart today:", simple_cart)

#However you can remove any individual item
simple_cart.remove("apples")
print("Here is my updated shopping cart today:", simple_cart)

# Since there is no ordering in a set, the items are not indexed
# Use for each to access the items one by one
for item in simple_cart:
    print("The next item in my cart is:", item)

#You can also create a set from a list or a tuple using the set() function
second_cart = set (("ketchup", "barbecue sauce","milk","bananas"))
print("I have also made a second cart:", second_cart)

# All set operations are supported.
# For a list see -- https://www.w3schools.com/python/python_sets_methods.asp
# For a more detailed explanation -- https://docs.python.org/3/library/stdtypes.html#set

# Let's see the union, see that bananas does not repeat itself in the union
unified_cart = simple_cart.union(second_cart)
print("My unified cart is:", unified_cart)

# You can also create a list from a set. 
unified_list = list (unified_cart)
print("My cart as a list is:", unified_list)

# You can go back to a set by re-using the set() function.
# Note that the order will not be necessarily what you expect. But it does not matter for a set. 
back_to_set = set (unified_list)
print("My cart is again a set:", back_to_set)

if(unified_cart == back_to_set):
    print("Two sets are equal")

# Python also has a related structure called a frozen set, which is immutable. This means you cannot add or remove items from this set.
finalized_cart = frozenset(unified_list)
print("Finalized cart:", finalized_cart)